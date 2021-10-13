#ifndef _TIFF_HPP
#define _TIFF_HPP

#include "bmp_256bpp.hpp"

class Tiff :
	public Bmp_256bpp
{
public:
	Tiff(void);
	Tiff(std::string inName, int inLength, int inWidth);
	~Tiff(void);

	virtual int getSize ( void ) const;
	virtual void Compress( void );
	virtual std::string toString( void );
};
#endif //_TIFF_HPP