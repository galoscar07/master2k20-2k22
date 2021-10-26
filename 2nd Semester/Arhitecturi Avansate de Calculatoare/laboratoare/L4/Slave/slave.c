#include <stdio.h>
#include "pvm3.h"

void main()
{
	int innum;
	int info;
	int data[6] = {1,2, 3, 4, 5, 6};

	innum = pvm_joingroup("Grup");

	Sleep(5000);


	info = pvm_reduce(PvmSum, data, 6, PVM_INT, 1, "Grup", innum);

	info = pvm_lvgroup("Grup");

	pvm_exit();
}