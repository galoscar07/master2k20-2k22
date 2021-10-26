#include <stdio.h>
#include "pvm3.h"

void main()
{
	int nr_procese;
	int slaves[5];
	int tid = pvm_mytid();
	int tid_slave;
	//char mesaj[15];
	printf("Identificator master = %d\n", tid);
	
	nr_procese = pvm_spawn("slave", NULL, PvmTaskDefault, "", 1, slaves);

	printf("Numarul de procese create este = %d\n", nr_procese);

	tid_slave = slaves[0];
	printf("Identificator slave = %d\n", tid_slave);

	pvm_notify(PvmTaskExit, 3, 1, slaves);

	pvm_recv(-1, 3);

	pvm_upkint(tid_slave, 1, 1);
	printf("Identificator proces terminat: %d\n", tid_slave);

	pvm_exit();
}