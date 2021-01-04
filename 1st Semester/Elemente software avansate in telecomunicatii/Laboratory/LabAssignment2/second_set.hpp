//
//  baza_deriv.hpp
//  LabAssignment2
//
//  Created by Gal Oscar on 18/10/2020.
//

#ifndef baza_deriv_hpp
#define baza_deriv_hpp

#include <stdio.h>
class Baza {
protected:
    int a, b;
public:
    Baza( ) { a = 1; b = 1; }
    void setA(int a) {
        this->a = a;
    }
    void setB(int b) {
        this->b = b;
    }
    int getA( ) {
        return a;
    }
    int getB( ) {
        return b;
    }
    int aduna( ) {
        return a + b;
    }
    int scade( ) {
        return a - b;
    }
};

class Derivata : private Baza {
public:
    int inmulteste() {
        return a * b;
    }
    int aduna( ) {
        return a + b;
    }
    int scade( ) {
        return a - b;
    }
};

#endif /* baza_deriv_hpp */
