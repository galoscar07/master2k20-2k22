
import ffmpeg


def flip_video_horizontally():
    stream = ffmpeg.input('result.avi')
    stream = ffmpeg.hflip(stream)
    stream = ffmpeg.output(stream, 'output.mp4')
    ffmpeg.run(stream)


def convert_mp4_to_mkv():
    ffmpeg.input('input.mp4').output('output.mkv').run()


if __name__ == '__main__':
    flip_video_horizontally()
    # convert_mp4_to_mkv()
