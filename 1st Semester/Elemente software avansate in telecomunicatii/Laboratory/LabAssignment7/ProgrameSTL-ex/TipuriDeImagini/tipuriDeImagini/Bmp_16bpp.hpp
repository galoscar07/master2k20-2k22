#ifndef _BMP_16BPP_HPP
#define _BMP_16BPP_HPP

#include "imagine.hpp"

class Bmp_16bpp :
	public Imagine
{
public:
	Bmp_16bpp(void);
	Bmp_16bpp(std::string, int, int);
	~Bmp_16bpp(void);

	virtual int getSize ( void ) const;
	virtual void Compress( void );
	virtual std::string toString( void );
};
#endif //_BMP_16BPP_HPP