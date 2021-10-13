// hash_mapEx.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <hash_map>

int main()
{
	std::hash_map <int, int> hm1, hm2, hm3;
	int i;
	typedef std::pair <int, int> Int_Pair;

	for ( i = 0 ; i < 3 ; i++ )
	{
		hm1.insert ( Int_Pair ( 3 , 3 ) );
		hm2.insert ( Int_Pair ( 3 - i, 3 - i * i ) );
		hm3.insert ( Int_Pair ( 3 - i, 3 - i ) );
	}

	std::cout << "hm1\n";
	for ( i = 0 ; i < 3 ; i++ )
	{
		std::cout << hm1[i];
	}
	std::cout << std::endl;

	std::cout << "hm2\n";
	for ( i = 0 ; i < 1 ; i++ )
	{
		std::cout << hm2[i];
	}
	std::cout << std::endl;

	std::cout << "hm3\n";
	for ( i = 0 ; i < 1 ; i++ )
	{
		std::cout << hm3[i];
	}
	std::cout << std::endl;

	if (hm1 != hm2)
		std::cout << "The hash_maps hm1 and hm2 are not equal." << std::endl;
	else
		std::cout << "The hash_maps hm1 and hm2 are equal." << std::endl;

	if (hm1 != hm3)
		std::cout << "The hash_maps hm1 and hm3 are not equal." << std::endl;
	else
		std::cout << "The hash_maps hm1 and hm3 are equal." << std::endl;

	return 0;
}

