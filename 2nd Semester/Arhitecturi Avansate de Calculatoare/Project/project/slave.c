#include <stdio.h>
#include "pvm3.h"


void main()
{
    int ai0, ai1, ai2, bj0, bj1, bj2, info;
    /* int Ai[3], Bj[3] */

    /* Se receptioneaza buffer-ul de la procesul parinte */
    info = pvm_recv(pvm_parent(), 1);
    /* Se preiau valorile pentru linea i din matricea A */
    info = pvm_upkint(&ai0, 1, 1);
    info = pvm_upkint(&ai1, 1, 1);
    info = pvm_upkint(&ai2, 1, 1);
    /* info = pvm_upkint(&Ai, 1, 1)  */
    
    /* Se preiau valorile pentru coloana j din matricea B */
    info = pvm_upkint(&bj0, 1, 1);
    info = pvm_upkint(&bj1, 1, 1);
    info = pvm_upkint(&bj2, 1, 1);
    /* info = pvm_upkint(&Bj, 1, 1)  */


    /* Se calculeaza inmultirea matricilor pentru valorile primite */
    result = ai0 * bj0 + ai1 * bj1 + ai2 * bj2;
    /* result = Ai[0] * Bj[0] + Ai[1] * Bj[1] + Ai[2] * Bj[2] */
    
    /* Se initializeaza buffer-ul de transmisie */
    info = pvm_initsend(PvmDataDefault);
    /* Se impacheteaza in buffer rezultatul obtinut care se afla in varibila 'c'. */
    info = pvm_pkint(&result, 1, 1);
    /* Se transmite rezultatul obtinut inapoit la procesul parinte. */
    info = pvm_send(pvm_parent(), 2);

    /* Se incheie procesul */
    pvm_exit();
}

