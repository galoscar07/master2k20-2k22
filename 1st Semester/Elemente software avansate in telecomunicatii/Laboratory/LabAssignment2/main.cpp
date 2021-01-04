//
//  main.cpp
//  LabAssignment2
//
//  Created by Gal Oscar on 18/10/2020.
//

#include <iostream>
using namespace std;
#include "first_set.hpp"
#include "second_set.hpp"
#include "third_set.hpp"


void run_first() {
    
    cout << "Din primul set de probleme problema 3" << "\n";
    
    Student gal_oscar = Student("Gal", "Oscar", "1");
    int note[4] = {10, 10, 10, 10};
    gal_oscar.set_note(note);
    Student badau_florica = Student("Badau", "Florica", "1");
    note[3] = 7;
    badau_florica.set_note(note);
    Student marian_alexandru = Student("Marian", "Alexandru", "1");
    note[0] = 3;
    note[2] = 5;
    marian_alexandru.set_note(note);
    Student florin_dumitrescu = Student("Florin", "Dumitrescu", "1");
    florin_dumitrescu.set_note(note);
    Student florin_scarlatescu = Student("Florin", "Scarlatescu", "1");
    note[0] = 10;
    note[2] = 6;
    florin_scarlatescu.set_note(note);
    Student geanina_alexandrescu = Student("Geanina", "Alexandrascu", "1");
    note[3] = 7;
    geanina_alexandrescu.set_note(note);
    
    Student students[] = {
        gal_oscar, badau_florica, marian_alexandru, florin_dumitrescu, florin_scarlatescu, geanina_alexandrescu
    };
    cout << "Studentii cu restante sunt: \n";
    int i;
    for (i = 0; i < 6; i++) {
        if (students[i].are_examene_restante()) {
            cout << students[i].get_full_name() << '\n';
        }
    }
    
    cout << "Studentii in ordinea mediilor sunt: \n";
    Student primul = students[0];
    Student aldoilea;
    Student altreilea;
    for (i = 1; i < 6; i++) {
        if (students[i].get_medie() > primul.get_medie()) {
            altreilea = aldoilea;
            aldoilea = primul;
            primul = students[i];
        } else if (students[i].get_medie() > aldoilea.get_medie()) {
            altreilea = aldoilea;
            aldoilea = students[i];
        } else if (students[i].get_medie() > altreilea.get_medie()) {
            altreilea = students[i];
        }
    }
    cout << "1. " << primul.get_full_name() << " - media: " << primul.get_medie() << "\n";
    cout << "2. " << aldoilea.get_full_name() << " - media: " << aldoilea.get_medie() << "\n";
    cout << "3. " << altreilea.get_full_name() << " - media: " << altreilea.get_medie() << "\n";
    
}

void run_second() {
    
    cout << "\nDin al doilea set de probleme problema 9" << "\n";
    Baza obiect_baza;
    cout << "\nAfis din baza (val. initiale): " << obiect_baza.getA( ) << " " << obiect_baza.getB( ) << '\n';
    cout << "\nSuma este (cu val. initiale, baza) = " << obiect_baza.aduna( ); // corect aduna( )
    cout << "\nDiferenta este (cu val. initiale, baza) = " << obiect_baza.scade( );
    obiect_baza.setA(2);
    obiect_baza.setB(3);
    cout << "\nAfis din baza (modificat): " << obiect_baza.getA( ) << " " << obiect_baza.getB( ) << '\n';
    cout << "\nSuma/Diferenta dupa setare= " <<obiect_baza.aduna( ) << "/"<< obiect_baza.scade( )<<'\n';
    Derivata obiect_derivat;
    cout << "\nProdusul este (din derivat cu val. initiale) = " << obiect_derivat.inmulteste( ) << '\n';
    cout << "\nSuma este (din derivat cu val. initiale, baza) = " << obiect_derivat.aduna( ) << '\n';
    cout << "Diferenta dupa setare= " << obiect_derivat.scade( ) << '\n';

}

void run_third() {
    cout << "\nDin al treilea set de probleme problema 9" << "\n";

    Vehicul monocicleta;
    Automobil ford;
    Camion semi;
    Barca barca_de_pescuit;
    monocicleta.mesaj( );
    monocicleta.set_greutate(123.12);
    cout << monocicleta.get_greutate() << "\n";
    ford.set_incarcatura_pasageri(12);
    ford.set_greutate(30);
    cout << ford.get_greutate() << "\n";
    ford.mesaj( );
    semi.mesaj( );
    barca_de_pescuit.mesaj( );
    cout << monocicleta.get_greutate();
    cout << ford.get_greutate();
    Vehicul *pmonocicleta;
    Automobil *pford;
    Camion *psemi;
    Barca *pbarca_de_pescuit;
    cout << "\n";
    pmonocicleta = &monocicleta;
    pmonocicleta->mesaj( );
    pford = &ford;
    pford->mesaj( );
    psemi = &semi;
    psemi->mesaj( );//din CB
    pbarca_de_pescuit = &barca_de_pescuit;
    pbarca_de_pescuit->mesaj( );
    cout << "\n";
    pmonocicleta = &monocicleta;
    pmonocicleta->mesaj( );
    pmonocicleta = &ford;
    pmonocicleta->mesaj( );
    pmonocicleta = &semi;
    pmonocicleta->mesaj( );
    pmonocicleta = &barca_de_pescuit;
    pmonocicleta->mesaj( );
}

int main(int argc, const char * argv[]) {
    run_first();
    run_second();
    run_third();
}

