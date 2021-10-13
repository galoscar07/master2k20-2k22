#ifndef _ATC_HPP
#define _ATC_HPP

#include "Aircraft.hpp"
#include "Runway.hpp"
#include <iostream>
#include <vector>
#include <string>

class ATC
{
public:
	ATC(void);
	ATC(const std::vector<Runway*>& Runways);
	~ATC(void);

	void Register(Aircraft* aircraft);
	void schedule(void);

private:
	std::vector<Runway*> Runways;
	std::vector<Aircraft*> aircraftsRegister;
};
#endif //_ATC_HPP