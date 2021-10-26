#include "Bigrunway.hpp"

BigRunway::BigRunway(void)
{
}

BigRunway::BigRunway(const long& ID, const long& length): mID(ID), mLength(length),
	mLengthAvailable(mLength), mLandingsAproved(0), mType("BigRunway")
{
}

BigRunway::~BigRunway(void)
{
}

long BigRunway::accept(const long& length)
{
	if (mLandingsAproved < 2)
	{
		if (mLengthAvailable >= length)
		{
			mLengthAvailable = mLength - length;
			mLandingsAproved++;
			if (mLandingsAproved == 1)
			{
				return  getID(); 
			}
			else
			{
				if (getID() < 18)
				{
					return getID() + 18;
				}
				else
				{
					return getID() - 18;
				}	
			}
		}
	}
	else
	{
	}

	return -1;
}

long BigRunway::getID(void) const
{
	return mID;
}

std::string BigRunway::getType(void) const
{
	return mType;
}