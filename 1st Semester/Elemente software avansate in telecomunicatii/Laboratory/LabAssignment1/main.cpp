#include <iostream>
#include <time.h>
#define EPS 1e-150

using namespace std;

double sqrt_1(double number) {
    // Descriere: Functia sqrt_1 va aplica sirul lui newtow pentru a calcula radicalul dintr-un numar.
    //     Daca numarul este unul subunitar sirul va incepe de la 1, iar daca numarul este
    //     unul supraunitar sirul va incepe de la numarul respectiv.
    // Date Intrare: number de tip double care este numarul din care extragem radical
    double X1, X2, y;
    if (number > 0 && number < 1) {
        X2 = 1;
    } else {
        X2 = number;
    }
    do {
        X1 = X2;
        X2 = 0.5 * (X1 + number / X1);
        if ((y = X1 - X2) < 0) {
            y = -y;
        }
    } while (y >= EPS);
    return X2;
}

double sqrt_2(double number) {
    // Descriere: Functia sqrt_2 calculeaza radicalul dintr-un numar inmultind radicalul inversului numarului cu numarul in sine.
    //     Radicalul va fi calculat tot cu metoda lui Newtown
    // Date Intrare: number de tip double care este numarul din care extragem radical
    double inverse = 1 / number;
    double X1, X2, y;
    X2 = 1;
    do {
        X1 = X2;
        X2 = 0.5 * (X1 + inverse / X1);
        if ((y = X1 - X2) < 0) {
            y = -y;
        }
    } while (y >= EPS);
    return X2 * number;
}


int main() {
    clock_t time1, time2; // Pentru a monitoriza cat dureaza executia metodelor
    cout << "Program pentru a calcula radicalul numerelor reale. Programul se va opri din executie la introducerea numarului 0" << "\n";
    while (true) { // Bucla pentru a mentine aplicatia in viata pana cand user-ul va introduce cifra 0
        double number; // Declaram numarul pe care il vom citi de la tastatura
        cout << "Numarul este: ";
        cin >> number;
        if (number < 0) { // Daca numarul este mai mic de 0 nu avem rezultat
            cout << "Nu se poate extrage radical din numar negativ in multimea reala" << "\n";
            continue;
        } else if (number == 0) { // Daca numarul este 0 rezultatul va fi 0
            cout << "Rezultat: 0" << "\n";
            exit(1);
        } else if (number == 1) { // Daca numarul este 1 rezultatul va fi 1
            cout << "Rezultat: 1" << "\n";
            continue;
        }
        
        // Pentru numere subunitare si supraunitare vom folosi prima metoda cea din laborator
        time1 = clock();
        cout << "Rezultat prima metoda: " << sqrt_1(number) << "\n";
        time1 = clock() - time1;
        cout << "Prima metoda a durat: " << time1 << " milisecunde \n";
        
        if (number > 1) {
            // Pentru numerele subunitare vom folosi si cea de-a doua metoda
            time2 = clock();
            cout << "Rezultat a doua metoda: " << sqrt_2(number) << "\n";
            time2 = clock() - time2;
            cout << "A doua metoda a durat: " << time1 << " milisecunde \n";
        }
    }
}
