
package mult_matrices;

import java.util.ArrayList;
import java.util.Scanner;


public class Mult_matrices {

    public static void main(String[] args) {
        ArrayList<Integer> x = new ArrayList<>();
        ArrayList<Double> y = new ArrayList<>();
        for (int col_row = 10; col_row <= 200; col_row += 10) {
            
            int[][] matriz1 = new int[col_row][col_row];
            int[][] matriz2 = new int[col_row][col_row];
            int[][] matriz3 = new int[col_row][col_row];

            for(int i = 0; i < col_row; i++){
                for(int j = 0; j < col_row; j++){
                    matriz1[i][j] = 1;
                    matriz2[i][j] = 2;
                }
            }

            double prom = 0;

            for (int l = 0; l < 10; l++) {
                long t_inicio, t_final;
                t_inicio = System.nanoTime();
                for (int i = 0; i < col_row; i++) {
                    for (int j = 0; j < col_row; j++) {
                        for (int k = 0; k < col_row; k++) {
                            matriz3[i][j] += matriz1[i][k]*matriz2[k][j];
                        }
                    } 
                }
                t_final = System.nanoTime();
                int elementos = col_row * col_row;
                double t = (t_final - t_inicio)/((col_row*elementos) + ((col_row - 1)*elementos));
                prom += t;
            }
            prom = prom / 10;
            x.add(col_row);
            y.add(prom);
        }
        
        System.out.println("Tamaño de la matriz = x");
        System.out.println("Tiempo promedio en hacer una operación (nano segundos = 10^-9) = y");
        
        for (int i = 0; i < 20; i++){ 
            System.out.println("x: " + x.get(i)+ " | y: " + y.get(i) + "\n ---------------");
             
        }
        
   
    }
    
}
