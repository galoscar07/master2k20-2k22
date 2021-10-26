#ifndef _IMAGINE_HPP
#define _IMAGINE_HPP

#include <iostream>
#include <string>
#include <windows.h>

class Imagine
{
public:
	Imagine(void);
	Imagine(std::string, int, int, int);
	virtual ~Imagine(void);

	virtual void Compress( void ) = 0;
	virtual std::string toString( void ) = 0;
	virtual int getSize ( void ) const = 0;

	void setLength ( const int& );
	void setWidth ( const int& );
	void setName ( const std::string& );

	int getLength ( void ) const;
	int getWidth ( void ) const;
	std::string getName ( void ) const;

private:
	int mLenght;
	int mWidht;
	std::string mName;
	const int bitsPerPixel;
};
#endif //_IMAGINE_HPP