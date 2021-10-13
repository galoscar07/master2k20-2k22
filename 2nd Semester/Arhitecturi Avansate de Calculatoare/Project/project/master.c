#include <stdio.h>
#include <stdlib.h>
#include "pvm3.h"

#define MATRIX_SIZE 3
#define TASK "slave"


/* Functia principala */
void main()
{
    int C[MATRIX_SIZE][MATRIX_SIZE];
    int tids[9], info, i, j, k;
    
    /* Se creeaza un numar de 9 procese si vor fi returnate in vectorul 'tids' */
    info = pvm_spawn(TASK, NULL, PvmTaskDefault, NULL, 9, tids);

    /* Se populeaza matricele */
    /* Matricea A */
    int A[MATRIX_SIZE][MATRIX_SIZE]= {{1,2,3},{2,3,4},{4,3,2}};
    /* Matricea B */
    int B[MATRIX_SIZE][MATRIX_SIZE] = {{4, 1, 2}, {1, 2, 3}, {4, 3, 2}}

    /* Transmisia catre procese */
    k = 0;
    for(i = 0; i < MATRIX_SIZE; i++)
    {
        for(j = 0; j < MATRIX_SIZE; j++)
        {
            /* Initializeza buffer-ul pentru trimitere + trimite elemente catre procesele slave */
            info = pvm_initsend(PvmDataDefault);
            /* Se incarca in buffer linia de pe pozitia i din matricea A*/
            info = pvm_pkint(&A[i][0], 1, 1);
            info = pvm_pkint(&A[i][1], 1, 1);
            info = pvm_pkint(&A[i][2], 1, 1);
            /* info = pvm_pack(&{A[i][0], A[i][1], A[i][2]}, 3, 1) */
            
            /* Se incarca in buffer coloana de pe pozitia j din matricea B*/
            info = pvm_pkint(&B[0][j], 1, 1);
            info = pvm_pkint(&B[1][j], 1, 1);
            info = pvm_pkint(&B[2][j], 1, 1);
            /* info = pvm_pack(&{B[0][j], B[2][j], B[3][j]}, 3, 1) */

            /* Se transmite buffer-ul catre procesul corespunzator. 1 este eicheta mesajului trimis*/
            info = pvm_send(tids[k++], 1);
        }
    }

    /* Se asteapta primirea mesajului de catre proces. */
    Sleep(1000);

    /* Receptia de la procese */
    k = 0;
    for(i = 0; i < MATRIX_SIZE; i++)
    {
        for(j = 0; j < MATRIX_SIZE; j++)
        {
            /* Se receptioneaza mesajul primit de la procesul corespunzator. 2 este eticheta mesajului primit */
            info = pvm_recv(tids[k++], 2);
            /* Se returneaza o singura valoare si se pune in 'C[i][j]' din buffer. */
            info = pvm_upkint(&C[i][j], 1, 1);
        }
    }

    /* Se afiseaza rezultatele obtinute */
    for (i = 0; i < MATRIX_SIZE; i++)
    {
        for (j = 0; j < MATRIX_SIZE; j++)
        {
            printf("%d ", C[i][j]));
        }
        printf("\n");
    }

    printf("\n");

    /* Se incheie procesul */
    pvm_exit();
}

