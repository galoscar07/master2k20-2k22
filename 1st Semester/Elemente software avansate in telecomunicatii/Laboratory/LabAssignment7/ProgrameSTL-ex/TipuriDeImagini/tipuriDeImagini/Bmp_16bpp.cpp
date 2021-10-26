#include "Bmp_16bpp.hpp"

Bmp_16bpp::Bmp_16bpp(void)
{
}

Bmp_16bpp::Bmp_16bpp(std::string inName, int inLength, int inWeight)
	:Imagine(inName, inLength, inWeight, 16)
{
}

Bmp_16bpp::~Bmp_16bpp(void)
{
}

int Bmp_16bpp::getSize ( void ) const
{
	return getLength () * getWidth () * 16;
}

void Bmp_16bpp::Compress( void )
{
	std::cout << "compressing a Bmp_16bpp...\n";
	Sleep(500);
}

std::string Bmp_16bpp::toString( void )
{
	return "";
}