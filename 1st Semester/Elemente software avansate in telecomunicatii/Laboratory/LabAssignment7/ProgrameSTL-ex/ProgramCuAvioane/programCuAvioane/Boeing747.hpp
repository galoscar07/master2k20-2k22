#ifndef _BOEING747_HPP
#define _BOEING747_HPP

#include "Aircraft.hpp"

class Boeing747 :
	public Aircraft
{
public:
	Boeing747(const long&);
	virtual ~Boeing747();

	virtual long getMinLandingLength(void) const;
	virtual void land(long RunwayID);
	virtual void hold(void);

private:
	long mLandingLength;
};
#endif //_BOEING747_HPP