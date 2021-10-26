#include "Gif.hpp"

Gif::Gif(void)
{
}

Gif::Gif(std::string inName, int inLength, int inWidth)
:Bmp_256bpp(inName, inLength, inWidth)
{
}

Gif::~Gif(void)
{
}

int Gif::getSize ( void ) const
{
	return Bmp_256bpp::getSize () * 0.3;
}

void Gif::Compress( void )
{
	std::cout << "compressing a Gif...\n";
	Sleep(500);
}

std::string Gif::toString( void )
{
	return "";
}