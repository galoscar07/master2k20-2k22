#ifndef _RUNWAY_HPP
#define _RUNWAY_HPP

#include <iostream>

class Runway
{
public:
	Runway(void);
	virtual ~Runway(void);

	virtual long accept(const long& length) = 0;
	virtual long getID(void) const = 0;
	virtual std::string getType(void) const = 0;
};
#endif //_RUNWAY_HPP