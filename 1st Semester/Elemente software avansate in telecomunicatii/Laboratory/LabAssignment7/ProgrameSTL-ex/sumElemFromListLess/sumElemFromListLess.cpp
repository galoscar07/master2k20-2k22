// sumElemFromListLess.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include "Sum.hpp"

void f(std::vector<int>&);

int main()
{
	std::vector<int> v;
	v.push_back(2);
	v.push_back(3);
	v.push_back(4);
	v.push_back(1);
	v.push_back(0);
	v.push_back(5);

	f(v);

	return 0;
}

void f(std::vector<int>& v)
{
	Sum s ;
	s = std::for_each (v.begin(), v.end(), s ); // invoke s() for each element of ld
	std::cout << "the sum is " << s.result() << "\n";
}