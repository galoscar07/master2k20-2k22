#include "Helicopter.hpp"

Helicopter::Helicopter(): mLandingLength(0)
{
	setName("Helicopter");
}

Helicopter::~Helicopter()
{

}

long Helicopter::getMinLandingLength(void) const
{
	return 0;
}

void Helicopter::land(long RunwayID)
{
	std::cout << "Aircraft Helicopter landing on runway " << RunwayID << "\n";
}

void Helicopter::hold(void)
{
	std::cout << "Aircraft Helicopter on hold\n";
}
