// dequeEx.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <deque>
#include <string>

int main()
{
	std::deque<std::string> d;
	std::deque<std::string>::iterator it;

	d.push_back("string1");
	d.push_back("string2");
	d.push_back("string3");
	d.push_front("string0");
	it = d.begin() + 3;
	d.insert(it + 3, "string10");

	it = d.begin();
	while (it != d.end())
	{
		std::cout << (*it) << "\n";
		it++;
	}

	//it = d.begin() + 3;
	//d.erase(it);
	//d.pop_back();
	//d.pop_front();
	it = d.begin();
	d.erase(it + 1);

	it = d.begin();
	while (it != d.end())
	{
		std::cout << (*it) << "\n";
		it++;
	}

	return 0;
}

