from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import numpy as np
import urllib
import cv2
import face_recognition
import os


@csrf_exempt
def detect(request):
    # initialize the data dictionary to be returned by the request
    data = {"success": False}
    # check to see if this is a post request
    if request.method == "POST":
        # check to see if an image was uploaded
        if request.FILES.get("image", None) is not None:
            # grab the uploaded image
            image = _grab_image(stream=request.FILES["image"])
        # otherwise, assume that a URL was passed in
        else:
            # grab the URL from the request
            url = request.POST.get("url", None)
            # if the URL is None, then return an error
            if url is None:
                data["error"] = "No URL provided."
                return JsonResponse(data)
            # load the image and convert
            image = _grab_image(url=url)

        # Get the training images and make a vector with them encoded
        train_images_path = 'face_detector/TrainImages'
        train_images = []
        class_names = []
        images_file_names_list = os.listdir(train_images_path)
        # myList = ['Billie Eilish.jpeg', 'Barack Obama.jpeg']

        for file_name in images_file_names_list:
            current_image = cv2.imread(f'{train_images_path}/{file_name}')
            train_images.append(current_image)
            class_names.append(os.path.splitext(file_name)[0])
        # classNames = ['Billie Eilish', 'Barack Obama']

        def find_encodings(images):
            """
            Find encoding will take as a param a list of images and return a list of encoded images
            """
            encode_list = []
            for image_to_encode in images:
                current_img = cv2.cvtColor(image_to_encode, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(current_img)[0]
                encode_list.append(encode)
            return encode_list

        encoded_train_images_list = find_encodings(train_images)

        faces_input_photo = face_recognition.face_locations(image)
        encoded_input_photo = face_recognition.face_encodings(image, faces_input_photo)

        for encode_face, face_location in zip(encoded_input_photo, faces_input_photo):
            matches = face_recognition.compare_faces(encoded_train_images_list, encode_face)
            face_distances = face_recognition.face_distance(encoded_train_images_list, encode_face)
            # face_distances - array containing how similar ar the encoded_train_images_list with encode_face
            match_index = np.argmin(face_distances)
            if matches[match_index]:
                resulted_name = class_names[match_index].upper()
                data.update({"success": True, "name": resulted_name})
            else:
                data.update({"success": False, "name": 'ERROR'})
        # update the data dictionary with the faces detected
    # return a JSON response
    return JsonResponse(data)


def _grab_image(path=None, stream=None, url=None):
    # if the path is not None, then load the image from disk
    if path is not None:
        image = cv2.imread(path)
    # otherwise, the image does not reside on disk
    else:
        # if the URL is not None, then download the image
        if url is not None:
            resp = urllib.urlopen(url)
            data = resp.read()
        # if the stream is not None, then the image has been uploaded
        elif stream is not None:
            data = stream.read()
        # convert the image to a NumPy array and then read it into
        # OpenCV format
        image = np.asarray(bytearray(data), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # return the image
    return image