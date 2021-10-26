#ifndef _BIGRUNWAY_HPP
#define _BIGRUNWAY_HPP

#include "runway.hpp"
#include <iostream>

class BigRunway :
	public Runway
{
public:
	BigRunway(void);
	BigRunway(const long& ID, const long& length);
	~BigRunway(void);

	virtual long accept(const long& length);
	virtual long getID(void) const;
	virtual std::string getType(void) const;
private:
	long mID;
	long mLength;
	long mLengthAvailable;
	short mLandingsAproved; //cate aterizari s-au alocat pe pista
	std::string mType;
};
#endif //_BIGRUNWAY_HPP