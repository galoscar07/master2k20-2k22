#ifndef _BMP_256BPP_HPP
#define _BMP_256BPP_HPP

#include "imagine.hpp"

class Bmp_256bpp :
	public Imagine
{
public:
	Bmp_256bpp(void);
	Bmp_256bpp(std::string, int, int);
	~Bmp_256bpp(void);

	virtual int getSize ( void ) const;
	virtual void Compress( void );
	virtual std::string toString( void );
};
#endif //_BMP_256BPP_HPP