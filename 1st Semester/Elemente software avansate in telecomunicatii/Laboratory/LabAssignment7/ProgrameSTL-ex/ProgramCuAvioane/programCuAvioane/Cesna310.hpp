#ifndef _CESNA310_HPP
#define _CESNA310_HPP

#include "Aircraft.hpp"

class Cesna310 : public Aircraft  
{
public:
	Cesna310(const long&);
	virtual ~Cesna310();

	virtual long getMinLandingLength(void) const;
	virtual void land(long RunwayID);
	virtual void hold(void);

private:
	long mLandingLength;

};
#endif //_CESNA310_HPP
