#include "Jpg.hpp"

Jpg::Jpg(void)
{
}

Jpg::Jpg(std::string inName, int inLength, int inWidth)
:Bmp_256bpp(inName, inLength, inWidth)
{
}

Jpg::~Jpg(void)
{
}

int Jpg::getSize ( void ) const
{
	return Bmp_256bpp::getSize () * 0.2;
}

void Jpg::Compress( void )
{
	std::cout << "compressing a Jpg...\n";
	Sleep(500);
}

std::string Jpg::toString( void )
{
	return "";
}