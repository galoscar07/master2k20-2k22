// mapEx.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <map>

void printMap(const std::map<int, std::string> months);

int main()
{
	std::map<int, std::string> months;
	std::map<int, std::string>::iterator it;

	months[16] = "June";
	months[16] = "June2";
	months[15] = "May";
	months[14] = "April";
	months[12] = "February";
	months[11] = "January";
	months[22] = "December";
	months[23] = "December";
	months[21] = "November";
	months[20] = "October";
	months[19] = "September";
	months[18] = "August";
	months[17] = "July";
	months.insert(std::pair<int, std::string>(0, "December"));
	it = months.find (0);

	printMap(months);

	std::cout << (*it).second.c_str () << "\n";

	//months.erase(15);

	//printMap(months);

	//it = months.find(14);
	//if (it != months.end())
	//	std::cout << (*it).second.c_str();
	//else
	//	std::cout << "nu exista";

	//months.insert( std::pair<int, std::string>(13, "MARTIE") );

	//printMap(months);

	return 0;
}

void printMap(const std::map<int, std::string> months)
{
	std::map<int, std::string>::const_iterator it;
	it = months.begin();
    while (it != months.end())
	{
		std::cout << (*it).second.c_str() << "\n";
		it++;
	}
	std::cout << std::endl;
}