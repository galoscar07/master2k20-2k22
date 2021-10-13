#include "ATC.hpp"

ATC::ATC(void)
{
}

ATC::ATC(const std::vector<Runway*>& Runways)
{
	this->Runways = Runways;

	std::vector<Runway*>::const_iterator it;
	it = Runways.begin();
	while (it != Runways.end())
	{
		std::cout << (*it)->getType() << " " << (*it)->getID() << "\n";
		it++;
	}
	std::cout << "\n";
}

ATC::~ATC(void)
{
}

void ATC::Register(Aircraft* inAircraft)
{
	std::cout << "Registering " << inAircraft->getName() << " Length " << inAircraft->getMinLandingLength() << "\n";
	aircraftsRegister.push_back(inAircraft);

/*	std::vector<Aircraft*>::iterator it;
	it = aircraftsRegister.begin();
	while (it != aircraftsRegister.end())
	{
		std::cout << (*it)->getMinLandingLength() << std::endl;
		it++;
	}
*/
}

void ATC::schedule(void)
{
	std::vector<Aircraft*>::iterator itA;
	std::vector<Runway*>::iterator itR;

	itA = aircraftsRegister.begin();
	int currentElemInAircrafts = 0;
	while (itA != aircraftsRegister.end())
	{
		currentElemInAircrafts++;
		int acceptRez = -1;
		itR = Runways.begin();
		while (itR != Runways.end())
		{
			acceptRez = (*itR)->accept((*itA)->getMinLandingLength());
			if (acceptRez != -1)
			{
				std::vector<Aircraft*>::iterator tempItA;
				(*itA)->land(acceptRez);
				break;
			}
			else
			{
			}

			itR++;
		}
		if (acceptRez == -1)
		{
			(*itA)->hold();
		}
		itA++;
	}
}