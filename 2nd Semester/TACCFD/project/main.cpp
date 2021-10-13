//
//  Created by Oscar
//

#include <string>
#include <iostream>
#include <vector>

struct Relay;

struct FirstPerson {
    // The first person that's gonna send through a message
    std::string nume = "Oscar";
    std::string data;

    std::vector<std::pair<std::string, std::string>> received_data;

    void send(Relay& r);
    void read_user_data() {
        std::cout << "Add the data that Oscar's gonna send to Cris \n";
        std::cout << "Oscar: ";
        std::getline(std::cin, data);
    }
};


struct SecondPerson {
    // The second person that's gonna send through a message
    std::string nume = "Cris";
    std::string data;

    std::vector<std::pair<std::string, std::string>> received_data;

    void send(Relay& r);
    void read_user_data()
    {
        std::cout << "Add the data that Cris's gonna send to Oscar \n";
        std::cout << "Cris: ";
        std::getline(std::cin, data);
    }
};


struct Relay {
    std::vector<std::pair<std::string, std::string>> data_relay;

    void send_first_person(FirstPerson& a, SecondPerson& b) {
        for (auto pair : data_relay) {
            if (pair.first.find(b.nume) != std::string::npos)
            {
                a.received_data.push_back(std::make_pair(pair.first, pair.second));
                std::cout << "Relay sends a message to " << a.nume << " from " << b.nume << "\n";
            }
        }
    }


    void send_second_person(FirstPerson& a, SecondPerson& b) {
        for (auto pereche : data_relay) {
            if (pereche.first.find(a.nume) != std::string::npos) {
                b.received_data.push_back(std::make_pair(pereche.first, pereche.second));
                std::cout << "Relay sends a message to " << b.nume << " from " << a.nume << "\n";
            }
        }

    }
};


void FirstPerson::send(Relay& r) {
    r.data_relay.push_back(std::make_pair(nume, data));
    std::cout << "\n The relay received a message from: " << nume << "\n";
};

void SecondPerson::send(Relay& r) {
    r.data_relay.push_back(std::make_pair(nume, data));
    std::cout << "\n The relay received a message from: " << nume << "\n";
};

int main() {
    FirstPerson a;
    SecondPerson b;
    Relay r;
    char stop = 'y';
    while (stop == 'y') {
        a.read_user_data();
        a.send(r);

        b.read_user_data();
        b.send(r);

        std::cout << "\n\t If you want to continue the conversation hit the key y else n: ";

        stop = std::cin.get();
        std::cin.ignore();

    }
    r.send_first_person(a, b);
    r.send_second_person(a, b);
    std::cout << "\n Oscar received: " << "\n";
    for (auto pereche : a.received_data)
        std::cout << pereche.first << ": " << pereche.second << "\n";

    std::cout << "\n Cirs received: " << "\n";
    for (auto pereche : b.received_data)
        std::cout << pereche.first << ": " << pereche.second << "\n";


}
