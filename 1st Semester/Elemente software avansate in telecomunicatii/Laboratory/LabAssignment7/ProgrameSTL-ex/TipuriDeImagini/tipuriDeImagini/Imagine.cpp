#include "Imagine.hpp"

Imagine::Imagine(void)
	:mName("default1"), mLenght(0), mWidht(0), bitsPerPixel(16)
{
}

Imagine::Imagine(std::string inName, int inLength, int inWeight, int inDepth)
	:mName(inName), mLenght(inLength), mWidht(inWeight), bitsPerPixel(inDepth)
{
}

Imagine::~Imagine(void)
{
}

void Imagine::setLength ( const int& inLength)
{
}

void Imagine::setWidth ( const int& inWidth)
{
}

void Imagine::setName ( const std::string& inName)
{
}

int Imagine::getLength ( void ) const
{
	return mLenght;
}

int Imagine::getWidth ( void ) const
{
	return mWidht;
}

std::string Imagine::getName ( void ) const
{
	return mName;
}