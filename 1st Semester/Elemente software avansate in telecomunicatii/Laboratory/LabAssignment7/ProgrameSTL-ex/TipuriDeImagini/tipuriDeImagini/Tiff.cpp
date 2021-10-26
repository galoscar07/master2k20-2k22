#include "Tiff.hpp"

Tiff::Tiff(void)
{
}

Tiff::Tiff(std::string inName, int inLength, int inWidth)
:Bmp_256bpp(inName, inLength, inWidth)
{
}

Tiff::~Tiff(void)
{
}

int Tiff::getSize ( void ) const
{
	return Bmp_256bpp::getSize () * 0.5;
}

void Tiff::Compress( void )
{
	std::cout << "compressing a Tiff...\n";
	Sleep(500);
}

std::string Tiff::toString( void )
{
	return "";
}