#include "Sum.hpp"

Sum::Sum(void): mRes(0)
{
}

Sum::Sum(int i = 0): mRes(i)
{
}

Sum::~Sum(void)
{
}

void Sum::operator()(int x)
{
	mRes += x;
}

int Sum::result() const
{
	return mRes;
}