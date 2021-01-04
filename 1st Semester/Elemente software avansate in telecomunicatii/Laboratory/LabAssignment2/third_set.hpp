//
//  third_set.hpp
//  LabAssignment2
//
//  Created by Gal Oscar on 18/10/2020.
//

#ifndef third_set_hpp
#define third_set_hpp

#include <stdio.h>
#include <iostream>
using namespace std;

class Vehicul {
    int roti;
    float greutate;
public:
    virtual void mesaj( ) {
        cout << "Mesaj din clasa Vehicul\n";
    }
    virtual void set_greutate(float greutate) {
        this->greutate = greutate;
    }
    virtual float get_greutate() {
        return this->greutate;
    }
};

class Automobil : public Vehicul {
    int incarcatura_pasageri;
public:
    void mesaj( ) override {
        cout << "Mesaj din clasa Automobil\n";
    }
    void set_incarcatura_pasageri(int incarcatura_pasageri) {
        this->incarcatura_pasageri = incarcatura_pasageri;
    }
    int get_incarcatura_pasageri() {
        return this->incarcatura_pasageri;
    }
    void set_greutate(float greutate) override {
        this->Vehicul::set_greutate(greutate + incarcatura_pasageri);
    }
    float get_greutate() override{
        return this->Vehicul::get_greutate();
    }
};

class Camion : public Vehicul {
    int incarcatura_pasageri;
    float incarcatura_utila;
public:
    int pasageri( ) {
        return incarcatura_pasageri;
    }
    void set_greutate(float greutate) override {
        this->Vehicul::set_greutate(greutate + incarcatura_pasageri + incarcatura_utila);
    }
    float get_greutate() override{
        return this->Vehicul::get_greutate();
    }
};

class Barca : public Vehicul {
    int incarcatura_pasageri;
public:
    int pasegeri( ){
        return incarcatura_pasageri;
    }
    void mesaj( ) override {
        cout << "Mesaj din clasa Barca\n";
    }
    void set_greutate(float greutate) override {
        this->Vehicul::set_greutate(greutate + incarcatura_pasageri);
    }
    float get_greutate() override{
        return this->Vehicul::get_greutate();
    }
};

#endif /* third_set_hpp */
