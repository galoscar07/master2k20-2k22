#ifndef _SMALLRUNWAY_HPP
#define _SMALLRUNWAY_HPP

#include "runway.hpp"
#include <iostream>

class SmallRunway :
	public Runway
{
public:
	SmallRunway(void);
	SmallRunway(const long& ID, const long& length);
	~SmallRunway(void);

	virtual long accept(const long& length);
	virtual long getID(void) const;
	virtual std::string getType(void) const;
private:
	long mID;
	long mLength;
	bool mAvailable; //se poate sau nu ateriza pe pista
	std::string mType;
};
#endif //_SMALLRUNWAY_HPP