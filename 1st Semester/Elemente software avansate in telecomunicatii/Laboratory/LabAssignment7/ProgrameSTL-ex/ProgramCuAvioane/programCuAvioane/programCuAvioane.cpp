// programCuAvioane.cpp : Defines the entry point for the console application.
//

#include "HeapTracer.hpp"
#include "Helicopter.hpp"
#include "Cesna310.hpp"
#include "Boeing747.hpp"
#include "ATC.hpp"
#include "Runway.hpp"
#include "BigRunway.hpp"
#include "SmallRunway.hpp"
#include "HelicopterLandingArea.hpp"
#include <iostream>
#include <vector>

int rmain()
{
	std::vector<Runway*> runwaysVector;
	//fac 1 BigRunway, 1 SmallRunway si un HeliPad
	HelicopterLandingArea* hr1 = new HelicopterLandingArea(5);
	runwaysVector.push_back(hr1);
	SmallRunway* sr1 = new SmallRunway(10, 500);
	runwaysVector.push_back(sr1);
	BigRunway* br1 = new BigRunway(15, 1500);
	runwaysVector.push_back(br1);

	ATC* atc = new ATC(runwaysVector);

	Boeing747* sirGeorgeWithe = new Boeing747(750);
	Boeing747* queenMary = new Boeing747(750);
	Cesna310* cesna1 = new Cesna310(500);
	Cesna310* cesna2 = new Cesna310(500);
	Helicopter* hely1 = new Helicopter();
	Helicopter* hely2 = new Helicopter();

	atc->Register(sirGeorgeWithe);
	atc->Register(queenMary);
	atc->Register(cesna1);
	atc->Register(cesna2);
	atc->Register(hely1);

	std::cout << std::endl;

	atc->schedule();

	delete (sirGeorgeWithe);
	delete (queenMary);
	delete (cesna1);
	delete (cesna2);
	delete (hely1);
	delete (hely2);
	//delete (hr1);
	//delete (sr1);
	//delete (br1);

	std::vector<Runway*>::iterator it;
	it = runwaysVector.begin();
	while (it != runwaysVector.end())
	{
		delete (*it);
		it++;
	}

	delete (atc);

	return 0;
}

int main()
{
	HeapTracer ht;
	rmain();
	ht.Dump();
	return 0;
}
