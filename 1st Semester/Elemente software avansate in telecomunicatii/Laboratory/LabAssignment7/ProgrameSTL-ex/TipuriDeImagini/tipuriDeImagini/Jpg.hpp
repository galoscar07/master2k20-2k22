#ifndef _JPG_HPP
#define _JPG_HPP

#include "bmp_256bpp.hpp"

class Jpg :
	public Bmp_256bpp
{
public:
	Jpg(void);
	Jpg(std::string inName, int inLength, int inWidth);
	~Jpg(void);

	virtual int getSize ( void ) const;
	virtual void Compress( void );
	virtual std::string toString( void );
};
#endif //_JPG_HPP