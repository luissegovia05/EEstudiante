/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.mycompany.condicionales;

import java.util.Scanner;

/**
 *
 * @author Sala de Sistemas 4
 */
public class Condicionales {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int opcion = entrada.nextInt();
        
     
        if(opcion >0 && opcion <05){
            System.out.println("es una opcion valida");
            
            
        }else{
            System.out.println("no es una opcion valida");
        }
      
        switch (opcion){
            case 1,2,3 -> System.out.println("1 es una opcion valida");
            default -> System.out.println("no es una opcion valida");
            
        }
    }
}
