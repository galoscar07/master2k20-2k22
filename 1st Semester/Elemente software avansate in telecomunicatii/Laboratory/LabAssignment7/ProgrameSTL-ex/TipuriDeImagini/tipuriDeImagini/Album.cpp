#include "Album.hpp"

Album::Album(void)
{
}

Album::~Album(void)
{
}

void Album::addImagine(Imagine* inInagine)
{
	imgVec.push_back(inInagine);
}

void Album::ShowImages(void)
{
	std::vector<Imagine*>::iterator it;

	it = imgVec.begin();
	while (it != imgVec.end())
	{
		std::cout << (*it)->getName () << " " << "size: " << (*it)->getSize() / 8
			<< "dim: " << (*it)->getLength() << "X" << (*it)->getWidth() << std::endl;
		++it;
	}
}

int Album::GetPicsNo ( void ) const 
{
	std::vector<Imagine*>::const_iterator it;
	int count = 0;

	it = imgVec.begin();
	while (it != imgVec.end())
	{
		++count;
		++it;
	}

	return count;
}

int Album::GetTotalSize ( void ) const
{
	std::vector<Imagine*>::const_iterator it;
	int count = 0;

	it = imgVec.begin();
	while (it != imgVec.end())
	{
		count += (*it)->getSize();
		++it;
	}

	return count;
}

int Album::GetPicsNo ( Types inType )
{
	int totalSize = 0;
	std::vector<Imagine*>::iterator it;

	it = imgVec.begin();
	while (it != imgVec.end())
	{
		switch ( inType )
		{
			case BMP_16BPP:
			{
				Bmp_16bpp* temp;
				temp = dynamic_cast<Bmp_16bpp*> (*it);
				if (temp != NULL)
				{
					++totalSize;
				}
				break;
			}
			case BMP_256BPP:
			{
				Bmp_256bpp* temp;
				temp = dynamic_cast<Bmp_256bpp*> (*it);
				if (temp != NULL)
				{
					++totalSize;
				}
				break;
			}
			case JPG:
			{
				Jpg* temp;
				temp = dynamic_cast<Jpg*> (*it);
				if (temp != NULL)
				{
					++totalSize;
				}
				break;
			}
			case GIF:
			{
				Gif* temp;
				temp = dynamic_cast<Gif*> (*it);
				if (temp != NULL)
				{
					++totalSize;
				}
				break;
			}
			case TIFF:
			{
				Tiff* temp;
				temp = dynamic_cast<Tiff*> (*it);
				if (temp != NULL)
				{
					++totalSize;
				}
				break;
			}
		}

		++it;
	}

	return totalSize;
}

Imagine* Album::GetPicsByName ( std::string inName )
{
	std::vector<Imagine*>::const_iterator it;

	it = find_if (imgVec.begin(), imgVec.end(), NameFind(inName));
	return (*it);

	//it = imgVec.begin();
	//while (it != imgVec.end())
	//{
	//	if ((*it)->getName().compare(inName) == 0)
	//	{
	//		return (*it);
	//	}
	//	else
	//	{
	//	}
	//	++it;
	//}

	return NULL;
}

void Album::SortByName ( void )
{
	Album::ByNameSort nameSort;
	std::sort(imgVec.begin(), imgVec.end(), nameSort);
}

void Album::SortBySize ( const bool down )
{
	if ( down )
	{
		Album::BySizeSort nameSort;
		std::sort(imgVec.begin(), imgVec.end(), nameSort);
	}
	else
	{
		Album::BySizeSortDown nameSort;
		std::sort(imgVec.begin(), imgVec.end(), nameSort);
	}
}

void Album::Compress ( void )
{
	std::vector<Imagine*>::const_iterator it;

	it = imgVec.begin();
	while (it != imgVec.end())
	{
		(*it)->Compress();
		++it;
	}
}

Album::ByNameSort::ByNameSort(void)
{
}

Album::ByNameSort::~ByNameSort(void)
{
}

bool Album::ByNameSort::operator () (const Imagine* inImg1, const Imagine* inImg2)
{
	return (inImg1->getName().compare(inImg2->getName()) < 0);
}

Album::BySizeSort::BySizeSort(void)
{
}

Album::BySizeSort::~BySizeSort(void)
{
}

bool Album::BySizeSort::operator () (const Imagine* inImg1, const Imagine* inImg2)
{
	return ( inImg1->getSize() < inImg2->getSize() );
}

Album::BySizeSortDown::BySizeSortDown(void)
{
}

Album::BySizeSortDown::~BySizeSortDown(void)
{
}

bool Album::BySizeSortDown::operator () (const Imagine* inImg1, const Imagine* inImg2)
{
	return ( inImg1->getSize() > inImg2->getSize() );
}

Album::NameFind::NameFind ( const std::string& inName): mName ( inName )
{
}

Album::NameFind::~NameFind ()
{
}

bool Album::NameFind::operator () ( const Imagine* inImg )
{
	return (mName == inImg->getName());
}