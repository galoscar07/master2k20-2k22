#include "Smallrunway.hpp"

SmallRunway::SmallRunway(void)
{
}

SmallRunway::SmallRunway(const long& ID, const long& length): mID(ID), mLength(length),
	mAvailable(true), mType("SmallRunway")
{
}

SmallRunway::~SmallRunway(void)
{
}

long SmallRunway::accept(const long& length)
{
	if (mAvailable && mLength >= length)
	{
		mAvailable = false;
		return getID();
	}
	return -1;
}

long SmallRunway::getID(void) const
{
	return mID;
}

std::string SmallRunway::getType(void) const
{
	return mType;
}