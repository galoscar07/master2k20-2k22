#include <stdio.h>
#include "pvm3.h"

/**
Masterul creeaza 4 procese slave. Masterul trimite catre fiecare proces slave un mesaj continand o valoare intreaga (<val>). 
Procesele slave receptioneaza mesajul si creeeaza un raspuns de forma: “Procesul slave <tid_slave> a receptionat valoarea <val>”. 
Apoi trimit raspunsul masterului, care il afiseaza pe ecran (deci masterul afiseaza-pe randuri diferite- 4 mesaje raspuns). 
*/

void main()
{
	int nr_procese;
	int slaves[4];
	int tid = pvm_mytid();
	int i;
	int data[4] = {1,2, 3, 4};
	char receivedData[100];

	//ID proces master
	printf("Identificator master = %d\n", tid);
	

	//se creaza procesele slave
	nr_procese = pvm_spawn("slave", NULL, PvmTaskDefault, "", 4, slaves);

	//afisam numarul de procese slave create
	printf("Numarul de procese create este = %d\n", nr_procese);

	printf("Se transmit datele cate slaves:\n");
	//Transmisia datelor catre procesele slave
	for(i = 0; i < 4; i++) {
		printf("%d\n", data[i]);
		//Se initializeaza bufferul de transmisie implicit.
		pvm_initsend(PvmDataDefault);
		//Se impacheteaza o valoare de tip intreg
		pvm_pkint(&data[i], 1, 1);
		//Se transmite bufferul catre procesul slave
		pvm_send(slaves[i], 2);
	}

	//Asteptam primirea mesajului de catre procesele slave
	Sleep(5000);
	
	//Primirea de la rpocesele slave
	for(i = 0; i < 4; i++) {
		//Se receptioneaza mesajul primit de la procesul slave corespunzator
		pvm_recv(slaves[i], 5);
		//Despachetam valoarea de tip string primita de la procesul slave
		pvm_upkstr(&receivedData, 1, 1);
		printf("%s\n", receivedData);
	}
	

	//Incheierea procesului 
	pvm_exit();
}