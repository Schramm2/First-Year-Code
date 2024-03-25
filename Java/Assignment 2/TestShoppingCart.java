// CSC1016S assignment 2
// Exercise 1
// Matthew Schramm
// SCHMAT041
// 2022-08-10
import java.util.Scanner;

public class TestShoppingCart{

   public static void main(String[] args) {
   Scanner input = new Scanner(System.in);
   int counter = 0;
   System.out.println("How many items would you like to add to your Shopping Cart?:");
   int items = input.nextInt();
   ShoppingCart cart1 = new ShoppingCart();
   if (items == 0){
      System.out.println("Your Shopping Cart is empty.");
   } else{
      while (counter != items){
      System.out.println("Enter the Product Name:");
      String prodName = input.next();
      System.out.println("Enter the Quantity:");
      int quantity = input.nextInt();
      System.out.println("Enter the Unit Cost:");
      double unitCost = input.nextDouble();
      Item product = new Item(prodName, quantity, unitCost);
      cart1.addItems(product);
      
      
      counter += 1;
      
      

      
      }
      System.out.println("The Shopping Cart has the following items:");
      cart1.queryCart();
      cart1.getDiscount("WELCOME20");
      System.out.println("--- Shopping Cart with all items ---");
      cart1.printInvoice();
      
      
   }
   












   }
}