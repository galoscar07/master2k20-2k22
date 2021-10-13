// listEx.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <list>

int main()
{
	std::list<int> l;
	std::list<int>::reverse_iterator rit;
	std::list<int>::iterator it;

	l.push_back(1);
	l.push_back(2);
	l.push_back(3);

	it = l.begin();
	it+= 2;
	l.erase(it);

	rit = l.rbegin();
	while (rit != l.rend())
	{
		std::cout << (*rit);
		++rit;
	}
	std::cout << std::endl;

	l.clear();

	rit = l.rbegin();
	while (rit != l.rend())
	{
		std::cout << (*rit);
		++rit;
	}
	std::cout << std::endl;

	l.push_back(4);
	l.push_back(5);
	l.push_back(6);

	rit = l.rbegin();
	while (rit != l.rend())
	{
		std::cout << (*rit);
		++rit;
	}
	std::cout << std::endl;

//	std::string delStr("s");
	l.remove(4);

	rit = l.rbegin();
	while (rit != l.rend())
	{
		std::cout << (*rit);
		++rit;
	}
	std::cout << std::endl;

	return 0;
}