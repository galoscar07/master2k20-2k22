#ifndef _GIF_HPP
#define _GIF_HPP

#include "bmp_256bpp.hpp"

class Gif :
	public Bmp_256bpp
{
public:
	Gif(void);
	Gif(std::string inName, int inLength, int inWidth);
	~Gif(void);

	virtual int getSize ( void ) const;
	virtual void Compress( void );
	virtual std::string toString( void );
};
#endif //_GIF_HPP