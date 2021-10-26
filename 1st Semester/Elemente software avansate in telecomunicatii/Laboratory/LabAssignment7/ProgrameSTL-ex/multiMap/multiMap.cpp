// multiMap.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <map>

int main()
{
	std::multimap<int, std::string> ms;
	std::multimap<int, std::string>::iterator it;

	ms.insert(std::pair<int, std::string>(0, "string0"));
	ms.insert(std::pair<int, std::string>(1, "string1"));
	ms.insert(std::pair<int, std::string>(1, "string1"));
	ms.insert(std::pair<int, std::string>(2, "string2"));
	ms.insert(std::pair<int, std::string>(3, "string3"));

	for (std::multimap<int, std::string>::iterator it = ms.begin(); it != ms.end(); ++it)
	{
		std::cout << (*it).second.c_str();
		std::cout << "\n";
	}
	std::cout << "\n";

	it = ms.find(1);

	if (it != ms.end())
		std::cout << (*it).second.c_str() << "\n";
	else
		std::cout << "nu exista\n";

	(*it).second = "str1";
	ms.insert(std::pair<int, std::string>(2, "str2"));

	for (std::multimap<int, std::string>::iterator it = ms.begin(); it != ms.end(); ++it)
	{
		std::cout << (*it).second.c_str();
		std::cout << "\n";
	}
	std::cout << "\n";

	ms.insert(std::pair<int, std::string>(7, "str7"));

	for (std::multimap<int, std::string>::iterator it = ms.begin(); it != ms.end(); ++it)
	{
		std::cout << (*it).second.c_str();
		std::cout << "\n";
	}
	std::cout << "\n";

	std::cout << "count 2:" << ms.count(2) << std::endl;

	ms.erase(2);

	for (std::multimap<int, std::string>::iterator it = ms.begin(); it != ms.end(); ++it)
	{
		std::cout << (*it).second.c_str();
		std::cout << "\n";
	}
	std::cout << "\n";

	return 0;
}

