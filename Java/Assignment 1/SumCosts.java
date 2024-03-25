import java.util.Scanner;

public class SumCosts
{
   public static void main(String [] args)
   {
   
   Currency rand = new Currency("R", "ZAR", 100);
   
   Scanner input = new Scanner(System.in);
   
   System.out.println("Enter an amount or '[D]one' to quit:");
   Money counter = new Money("R0",rand);

   String randAsk = input.next();
      while (!randAsk.equals("Done") && !randAsk.equals("D")) 
   {
         Money randAsked1 = new Money(randAsk, rand);
         counter = counter.add(randAsked1);
   

         System.out.println("Enter an amount or '[D]one' to print the sum and quit:");
         
         randAsk = input.next();
         
           
         
         
         

         
         


    } 
    System.out.println("Total: " + counter.toString());
   
         
         
         
   
   
   }
}