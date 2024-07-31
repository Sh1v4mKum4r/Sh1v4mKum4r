/*
 * 
 * This program solves a problem of,
 * printing a butterfly pattern of stars and spaces as per the input in a single loop.
 * 
 * for the input 10, the output will be:
 * 
 * 
 * The pattern is as follows:
 * 
 * *                *
 * **              **
 * ***            ***
 * ****          ****
 * *****        *****
 * ******      ******
 * *******    *******
 * ********  ********
 * ******************
 * ******************
 * ********  ********
 * *******    *******
 * ******      ******
 * *****        *****
 * ****          ****
 * ***            ***
 * **              **
 * *                *
 * 
 */

 import java.util.Scanner;
 class test{
     public static void main(String []args){
         Scanner sc=new Scanner(System.in);
         int n=sc.nextInt();sc.close(); //pretty basic input
         String star="*",space="  ".repeat(n-1);
         for(int i=0;i<=n*2;i++,star=(i<=n)?star+"*":star.substring(0,star.length()-1),space=(i<=n+1)?space.replaceFirst("  ",""):space+"  ") //main increment and decrement logic
             if(i!=n)System.out.println(star+space+star); //printing the pattern
     }
 }