// setEx2.cpp : Defines the entry point for the console application.
//

#include <iostream>

struct ltstr
{
	bool operator()(const char* s1, const char* s2) const
	{
		return strcmp(s1, s2) < 0;
	}
};

int main()
{
	const int N = 6;
	const char* a[N] = {"isomer", "ephemeral", "prosaic", 
						"nugatory", "artichoke", "serif"};
	const char* b[N] = {"flat", "this", "artichoke",
						"frigate", "prosaic", "isomer"};

	set<const char*, ltstr> A(a, a + N);
	set<const char*, ltstr> B(b, b + N);
	set<const char*, ltstr> C;

	cout << "Set A: ";
	copy(A.begin(), A.end(), ostream_iterator<const char*>(cout, " "));
	cout << endl;
	cout << "Set B: ";
	copy(B.begin(), B.end(), ostream_iterator<const char*>(cout, " "));   
	cout << endl;

	cout << "Union: ";
	set_union(A.begin(), A.end(), B.begin(), B.end(),
			ostream_iterator<const char*>(cout, " "),
			ltstr());   
	cout << endl;

	cout << "Intersection: ";
	set_intersection(A.begin(), A.end(), B.begin(), B.end(),
					ostream_iterator<const char*>(cout, " "),
					ltstr());    
	cout << endl;

	set_difference(A.begin(), A.end(), B.begin(), B.end(),
					inserter(C, C.begin()),
					ltstr());
	cout << "Set C (difference of A and B): ";
	copy(C.begin(), C.end(), ostream_iterator<const char*>(cout, " "));
	cout << endl;

	return 0;
}