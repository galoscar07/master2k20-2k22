//
//  Student.cpp
//  LabAssignment2
//
//  Created by Gal Oscar on 18/10/2020.
//

#include "first_set.hpp"

Student::Student() {}

Student::Student(string nume_input, string prenume_input, string grupa_input) {
    nume = nume_input;
    prenume = prenume_input;
    grupa = grupa_input;
}

void Student::set_note(int note_input[4]) {
    int i;
    for (i = 0; i < 4; i++) {
        note[i] = note_input[i];
    }
}
string Student::get_full_name() {
    return nume + " " + prenume;
}

string Student::get_nume() {
    return nume;
}
string Student::get_grupa() {
    return grupa;
}
string Student::get_prenume() {
    return prenume;
}

bool Student::are_examene_restante() {
    int i;
    for (i = 0; i < 4; i++) {
        if (note[i] < 4) {
            return true;
        }
    }
    return false;
}

double Student::get_medie() {
    return (double)(note[0] + note[1] + note[2] + note[3]) / 4;
}
