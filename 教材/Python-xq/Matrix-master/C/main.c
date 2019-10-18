#include <stdio.h>
#include <time.h>

int main()
{
    int x[20];
    double y[20];
    int posicion = 0;
    int col_row;
    int m;
    int i;
    int j;
    int k;
    for(col_row = 10; col_row <=200; col_row += 10){


        // se crean las matrices de dimensiones col_row x col_row
        int matriz1[col_row][col_row];
        int matriz2[col_row][col_row];
        int matriz3[col_row][col_row];

        // se llenan las matrices 1 y 2
        for(i = 0; i < col_row; i++){
            for(j = 0; j < col_row; j++){
                matriz1[i][j] = 1;
                matriz2[i][j] = 2;
            }
        }

        //se inicializan las variables de tiempo
        clock_t t_comienzo, t_final;
        double prom = 0;

        for(m = 0; m < 10; m++){ // se repite la multiplicación 10 veces
            t_comienzo = clock();
            for(i = 0; i < col_row; i++){
                for(j = 0; j < col_row; j++){
                    matriz3[i][j] = 0;
                    for(k = 0; k < col_row; k++){
                        matriz3[i][j] += matriz1[i][k]* matriz2[k][j];
                    }
                }
            }
            t_final = clock();
            int elementos = col_row*col_row;
            double t = ((double)(t_final - t_comienzo)/CLOCKS_PER_SEC)*1000;
            prom += t / ((col_row*elementos) + ((col_row - 1)*elementos));
        }

        prom = prom / 10;

        x[posicion] = col_row;
        y[posicion] = prom;
        posicion++;


    }

    for(i = 0; i < 20; i++){
        printf("x = %d", x[i]);
        printf(" y = %f milisegundos\n", y[i]);
    }

}
