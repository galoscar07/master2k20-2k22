#ifndef _AIRCRAFT_HPP
#define _AIRCRAFT_HPP

#include <iostream>

class Aircraft
{
public:
	Aircraft(void);
	~Aircraft(void);

	virtual long getMinLandingLength(void) const = 0;
	virtual void land(long RunwayID) = 0;
	virtual void hold(void) = 0;
	void setName(const std::string&);
	std::string getName(void) const;
private:
//	virtual void broadcastSOS(void) = 0;
	std::string className;
};
#endif //_AIRCRAFT_HPP