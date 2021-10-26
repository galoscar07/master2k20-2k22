#include "Bmp_256bpp.hpp"

Bmp_256bpp::Bmp_256bpp(void)
{
}

Bmp_256bpp::Bmp_256bpp(std::string inName, int inLength, int inWeight)
	:Imagine(inName, inLength, inWeight, 256)
{
}

int Bmp_256bpp::getSize ( void ) const
{
	return getLength () * getWidth () * 256;
}

Bmp_256bpp::~Bmp_256bpp(void)
{
}

void Bmp_256bpp::Compress( void )
{
	std::cout << "compressing a Bmp_256bpp...\n";
	Sleep(500);
}

std::string Bmp_256bpp::toString( void )
{
	return "";
}