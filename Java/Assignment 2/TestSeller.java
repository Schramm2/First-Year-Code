// CSC1016S assignment 2
// Exercise 1
// Matthew Schramm
// SCHMAT041
// 2022-08-10
import java.util.Scanner;

public class TestSeller{

   public static void main(String[] args) {
   Currency rand = new Currency("R", "ZAR", 100);
   System.out.println("Please enter the details of the seller.");
   Scanner input = new Scanner(System.in);
   
   System.out.print("ID: ");
   String iD1 = input.next();
   
   System.out.print("Name: ");
   String name1 = input.next();
   
   System.out.print("Location: ");
   String location1 = input.next();
   input.nextLine();
   System.out.print("Product: ");
   String product1 = input.nextLine();
   
   System.out.print("Price: ");
   String priceFull1 = input.next();
   
   
   Money price1 = new Money(priceFull1 ,rand);
   
   System.out.print("Units: ");
   int units = input.nextInt();
   
   Seller seller = new Seller(iD1, name1, location1, product1, rand, price1, units);
   
   System.out.println("The seller has been successfully created:");
   System.out.println("ID of the seller: "+ seller.iD);
   System.out.println("Name of the seller: "+ seller.name);
   System.out.println("Location of the seller: "+ seller.location);
   System.out.println("The product to sell: "+ seller.product);
   System.out.println("Product unit price: "+ seller.unit_price);
   System.out.println("The number of available units: "+ seller.number_of_units);
   

   
   




   
   










   }
}
