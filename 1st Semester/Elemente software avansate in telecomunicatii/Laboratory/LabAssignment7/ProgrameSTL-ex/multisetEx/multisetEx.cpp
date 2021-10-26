// multisetEx.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <set>

int main()
{
	std::multiset<int> ms;
	std::multiset<int>::iterator it;

	ms.insert(0);
	ms.insert(3);
	ms.insert(6);
	ms.insert(3);
	ms.insert(2);

	for (std::multiset<int>::iterator it = ms.begin(); it != ms.end(); ++it)
	{
		std::cout << (*it);
	}
	std::cout << "\n";

	it = ms.find(2);

	if (it != ms.end())
		std::cout << (*it);
	else
		std::cout << "nu exista\n";

	(*it) = 7;
	ms.insert(2);

	for (std::multiset<int>::iterator it = ms.begin(); it != ms.end(); ++it)
	{
		std::cout << (*it);
	}
	std::cout << "\n";

	ms.insert(7);

	for (std::multiset<int>::iterator it = ms.begin(); it != ms.end(); ++it)
	{
		std::cout << (*it);
	}
	std::cout << "\n";

	std::cout << "count 2:" << ms.count(2) << std::endl;

	for (std::multiset<int>::iterator it = ms.begin(); it != ms.end(); ++it)
	{
		std::cout << (*it);
	}
	std::cout << "\n";

	ms.erase(3);

	for (std::multiset<int>::iterator it = ms.begin(); it != ms.end(); ++it)
	{
		std::cout << (*it);
	}
	std::cout << "\n";

	return 0;
}

