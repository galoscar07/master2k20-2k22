#include "Boeing747.hpp"

Boeing747::Boeing747(const long& inLength): mLandingLength(inLength)
{
	setName("Boeing747");
}

Boeing747::~Boeing747()
{

}

long Boeing747::getMinLandingLength(void) const
{
	return mLandingLength;
}

void Boeing747::land(long RunwayID)
{
	std::cout << "Aircraft Boeing 747 landing on runway " << RunwayID << "\n";
}

void Boeing747::hold(void)
{
	std::cout << "Aircraft Boeing 747 on hold\n";
}
