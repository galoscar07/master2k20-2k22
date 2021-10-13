#include <stdio.h>
#include "pvm3.h"

void main()
{
	int nr_procese;
	int slaves[5];
	int tid = pvm_mytid();
	char mesaj[15];
	printf("Identificator master = %d\n", tid);
	
	nr_procese = pvm_spawn("slave", NULL, PvmTaskDefault, "", 1, slaves);

	printf("Numarul de procese create este = %d\n", nr_procese);

	pvm_recv(slaves[0], 5);

	pvm_upkstr(mesaj);
	printf("%s\n", mesaj);

	pvm_exit();
}