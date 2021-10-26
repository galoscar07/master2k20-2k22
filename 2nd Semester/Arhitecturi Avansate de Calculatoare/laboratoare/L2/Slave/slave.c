#include <stdio.h>
#include "pvm3.h"

void main()
{
	char *text = "Hello World!!";

	pvm_initsend(PvmDataDefault);

	pvm_pkstr(text);

	pvm_send(pvm_parent(), 5);

	pvm_exit();
}