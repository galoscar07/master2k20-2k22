#include "Aircraft.hpp"

Aircraft::Aircraft(void)
{
}

Aircraft::~Aircraft(void)
{
}

void Aircraft::setName(const std::string& inName)
{
	className = inName;
}

std::string Aircraft::getName(void) const
{
	return className;
}