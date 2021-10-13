// setEx.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <set>

//struct comparatie
//{
//	bool operator<(const std::string &arg1, const std::string &arg2)
//	{
//		if (strcmp(arg1.c_str(), arg2.c_str()) == 0) return true else return false;
//	}
//};

int main()
{
	std::set<int> set1;
	std::set<int>::iterator it;

	set1.insert(1);
	set1.insert(2);
	set1.insert(2);
	set1.insert(3);
	set1.insert(2);

	//it = set1.find(4);
	//(*it) = 0;
	//it = set1.find(4);
	//if (it != set1.end())
	//	std::cout << (*it);
	//else
	//	std::cout << "NU exista elem in lista!\n";

	it = set1.begin();
	while (it != set1.end())
	{
		std::cout << (*it);
		it++;
	}
	std::cout << std::endl;

	return 0;
}

//bool comparatie::operator<(const std::string s2) const
//{
//}
