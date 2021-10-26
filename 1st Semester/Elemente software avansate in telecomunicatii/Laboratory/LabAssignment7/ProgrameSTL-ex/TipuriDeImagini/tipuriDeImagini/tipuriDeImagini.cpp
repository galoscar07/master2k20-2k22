// tipuriDeImagini.cpp : Defines the entry point for the console application.
//

#include "Imagine.hpp"
#include "Bmp_16bpp.hpp"
#include "Bmp_256bpp.hpp"
#include "Jpg.hpp"
#include "Gif.hpp"
#include "Tiff.hpp"
#include "Album.hpp"
#include <iostream>

int main()
{
	Imagine* img1 = new Bmp_16bpp("imagineBmp16bpp", 640, 480);
	Imagine* img2 = new Bmp_256bpp("imagineBmp256bpp", 640, 480);
	Imagine* img3 = new Jpg("imagineJpg", 640, 480);
	Imagine* img4 = new Gif("imagineGif", 640, 480);
	Imagine* img5 = new Tiff("imagineTiff", 640, 480);
	Imagine* img6 = new Bmp_16bpp("imagineBmp16bpp2", 640, 480);
	Imagine* img7 = new Bmp_256bpp("imagineBmp256bpp2", 640, 480);
	Imagine* img8 = new Jpg("imagineJpg2", 640, 480);
	Imagine* img9 = new Gif("imagineGif2", 640, 480);
	Imagine* img10 = new Tiff("imagineTiff2", 640, 480);
	Imagine* img11 = new Bmp_256bpp("imagineBmp256bpp3", 640, 480);
	Imagine* img12 = new Jpg("imagineJpg3", 640, 480);

	Album* album1 = new Album();
	album1->addImagine(img1);
	album1->addImagine(img2);
	album1->addImagine(img3);
	album1->addImagine(img4);
	album1->addImagine(img5);

	album1->addImagine(img6);
	album1->addImagine(img7);
	album1->addImagine(img8);
	album1->addImagine(img9);
	album1->addImagine(img10);

	album1->addImagine(img11);
	album1->addImagine(img12);

	std::cout << "Afisez imaginile din album\n";
	std::cout << "--------------------------\n";
	album1->ShowImages();

	std::cout << "\nNr total de imagini: " << album1->GetPicsNo() <<"\n";

	std::cout << "Spatiul total ocupat de album: " << album1->GetTotalSize() / 8 << " bytes\n";

	std::cout << "Nr total de imagini Bmp_16bpp: " << album1->GetPicsNo(BMP_16BPP) <<"\n";
	std::cout << "Nr total de imagini Jpg: " << album1->GetPicsNo(JPG) << "\n";

	Imagine* tempImg = album1->GetPicsByName("imagineGif2");
	if ( tempImg )
	{
		std::cout << "\n" << tempImg->getName() << " " << tempImg->getLength() 
			<< "X" << tempImg->getWidth() << "\n";
	}
	else
	{
		std::cout << "\nNu exista imagine cu respectivul nume\n";
	}

	std::cout << "Afisez imaginile din album ordonate dupa nume\n";
	std::cout << "---------------------------------------------\n";
	album1->SortByName();
	album1->ShowImages();

	std::cout << "Afisez imaginile din album ordonate crescator dupa dimensiune\n";
	std::cout << "-------------------------------------------------------------\n";
	album1->SortBySize(false);
	album1->ShowImages();

	std::cout << "Afisez imaginile din album ordonate descrescator dupa dimensiune\n";
	std::cout << "----------------------------------------------------------------\n";
	album1->SortBySize(true);
	album1->ShowImages();

	std::cout << "Comprim imaginile\n";
	std::cout << "-----------------\n";
	album1->Compress();

	return 0;
}

