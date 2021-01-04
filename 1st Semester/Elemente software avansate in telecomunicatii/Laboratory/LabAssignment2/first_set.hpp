//
//  Student.hpp
//  LabAssignment2
//
//  Created by Gal Oscar on 18/10/2020.
//

#ifndef Student_hpp
#define Student_hpp

#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;


class Student {
    string nume;
    string prenume;
    string grupa;
    int note[4];
public: // membri publici
    Student();
    Student(string nume, string prenume, string grupa);
    void set_note(int note[]);
    string get_full_name();
    string get_nume();
    string get_grupa();
    string get_prenume();
    bool are_examene_restante();
    double get_medie();
};


#endif /* Student_hpp */
