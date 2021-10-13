#ifndef _HELICOPTER_HPP
#define _HELICOPTER_HPP

#include "Aircraft.hpp"

class Helicopter : public Aircraft  
{
public:
	Helicopter();
	virtual ~Helicopter();

	virtual long getMinLandingLength(void) const;
	virtual void land(long RunwayID);
	virtual void hold(void);

private:
	long mLandingLength;
};

#endif //_HELICOPTER_HPP
