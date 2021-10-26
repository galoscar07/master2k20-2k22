#include <stdio.h>
#include <string.h>
#include "pvm3.h"

void main()
{
	char text[100] = "Procesul slave ";
	char text2[] = " a receptionat valoarea ";
	char id[20];
	char val[5];

	int tid, received;

	//tid-ul procesului slave
	tid = pvm_mytid();

	//se primesc datele de la procesul master
	pvm_recv(pvm_parent(), 2);
	pvm_upkint(&received, 1, 1);

	//procesarea mesajului - cast din int la string si crearea mesajului final care va fi trimis la master
	sprintf(id, "%d", tid);

	sprintf(val, "%d", received);

	strcat(text, id);
	strcat(text, text2);
	strcat(text, val);

	//initializarea bufferului de transmisie
	pvm_initsend(PvmDataDefault);
	//impachetarea mesajului ca string, acesta va fi trimis la procesul master
	pvm_pkstr(text);
	//trimiterea mesajului la procesul master, eticheta 5
	pvm_send(pvm_parent(), 5);

	pvm_exit();
}