#include "Cesna310.hpp"

Cesna310::Cesna310(const long& inLength): mLandingLength(inLength)
{
	setName("Cesna310");
}

Cesna310::~Cesna310()
{

}

long Cesna310::getMinLandingLength(void) const
{
	return mLandingLength;
}

void Cesna310::land(long RunwayID)
{
	std::cout << "Aircraft Cesna310 landing on runway " << RunwayID << "\n";
}

void Cesna310::hold(void)
{
	std::cout << "Aircraft Cesna310 on hold\n";
}
