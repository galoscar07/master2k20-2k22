#include "Helicopterlandingarea.hpp"

HelicopterLandingArea::HelicopterLandingArea(void)
{
}

HelicopterLandingArea::HelicopterLandingArea(const long& ID): mID(ID), mLength(0),
	mAvailable(true), mType("HelicopterLandingArea")
{
}

HelicopterLandingArea::~HelicopterLandingArea(void)
{
}

long HelicopterLandingArea::accept(const long& length)
{
	if (mAvailable && length == 0)
	{
		mAvailable = false;
		return getID();
	}
	return -1;
}

long HelicopterLandingArea::getID(void) const
{
	return mID;
}

std::string HelicopterLandingArea::getType(void) const
{
	return mType;
}