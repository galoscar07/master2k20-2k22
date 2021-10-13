#ifndef _HELICOPTERLANDINGAREA_HPP
#define _HELICOPTERLANDINGAREA_HPP

#include "runway.hpp"
#include <iostream>

class HelicopterLandingArea :
	public Runway
{
public:
	HelicopterLandingArea(void);
	HelicopterLandingArea(const long& ID);
	~HelicopterLandingArea(void);

	virtual long accept(const long& length);
	virtual long getID(void) const;
	virtual std::string getType(void) const;
private:
	long mID;
	long mLength;
	bool mAvailable; //cate aterizari s-au alocat pe pista
	std::string mType;
};
#endif //_HELICOPTERLANDINGAREA_HPP