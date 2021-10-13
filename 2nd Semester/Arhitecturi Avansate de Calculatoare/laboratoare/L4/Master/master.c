#include <stdio.h>
#include "pvm3.h"

void main()
{
	int nr_procese;
	int slaves[5];
	int tid = pvm_mytid();
	//int tid_slave;
	int innun;
	int info;
	int i;
	int data[6] = {1,2, 3, 4, 5, 6};

	printf("Identificator master = %d\n", tid);
	
	innun = pvm_joingroup("Grup");
	printf("Numarul instantei= %d\n", innun);

	nr_procese = pvm_spawn("slave", NULL, PvmTaskDefault, "", 1, slaves);

	printf("Numarul de procese create este = %d\n", nr_procese);

	Sleep(5000);

	info = pvm_reduce(PvmSum, data, 6, PVM_INT, 1, "Grup", innun);

	Sleep(5000);

	for(i = 0; i < 6; i++) {
		printf("%d\n", data[i]);
	}

	info = pvm_lvgroup("Grup");

	/*
	tid_slave = slaves[0];
	printf("Identificator slave = %d\n", tid_slave);

	pvm_notify(PvmTaskExit, 3, 1, slaves);

	pvm_recv(-1, 3);

	pvm_upkint(tid_slave, 1, 1);
	printf("Identificator proces terminat: %d\n", tid_slave);
	*/

	pvm_exit();
}