import java.util.Arrays;
import java.util.List;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
public class Question1{
   public static void main ( String args [] )
   {
     Scanner input = new Scanner(System.in);
     
     System.out.println("Welcome to Great International Technology");
     char choice = 'z';
     int counter1 = 0;
     //int counter2 = 0;
     //int counter3 = 0;
     ComputerBox[] cBoxes = new ComputerBox[10];
     while(choice != 'q' || choice != 'Q'){
         //Box[] boxes = new Box[10];
         //Screen[] screens =run new Screen[10];
         //Accessory[] accessories = new Accessory[10];
         
         
         System.out.println("MENU: add (B)ox, add (S)creen, add (A)ccessories, (D)elete, (L)ist, (Q)uit");
         String choiceS = input.next().toLowerCase();
         choice = choiceS.charAt(0);
         
         if (choice == 'b'){
            
            System.out.println("Enter the serial number");
            
            String serialNo = input.next();
            
            
            System.out.println("Enter the manufacturer");
            input.nextLine();
            String manufacturer = input.nextLine();
            
            
            
            System.out.println("Enter the colour");
            String colour = input.nextLine();
            
            
           
            System.out.println("Enter the amount of memory (MB)");
            
            int memory = input.nextInt();
            
            
            ComputerBox box = new Box(serialNo, manufacturer, colour, memory);
            
            cBoxes[counter1] = box;
            
            
            System.out.println("Done");
            counter1 += 1;
            
            
         } else if (choice == 's'){
            
            System.out.println("Enter the serial number");
            String serialNo = input.next();
            
            System.out.println("Enter the manufacturer");
            String manufacturer = input.next();
            
            System.out.println("Enter the colour");
            input.nextLine();
            String colour = input.nextLine();
            
            System.out.println("Enter the screen size in inches");
            int size = input.nextInt();
            
            ComputerBox screen = new Screen(serialNo, colour, manufacturer, size);
            
            cBoxes[counter1] = screen;
            System.out.println("Done");
            
            counter1 += 1;

         } else if (choice == 'a'){
            
            System.out.println("Enter the serial number");
            String serialNo = input.next();
            
            System.out.println("Enter the manufacturer");
            String manufacturer = input.next();
            
            System.out.println("Enter the colour");
            input.nextLine();
            String colour = input.nextLine();
            
            
            
            ComputerBox acc = new Accessory(serialNo, manufacturer, colour);
            
            cBoxes[counter1] = acc;
            System.out.println("Done");
            
            counter1 += 1;

         } else if (choice == 'd'){
            System.out.println("Enter the serial number");
            String serialNo = input.next();
            counter1 -= 1;
            boolean found = true;
            for(int i = 0; i < counter1; i++){
               
               if(cBoxes[i].getSerialNo().equals(serialNo)){
                  found = true;
                  ComputerBox[] cBoxesNew = new ComputerBox[cBoxes.length - 1];
                  for (int j = 0, k = 0; j < cBoxes.length; j++) {
                     if(j == i){
                        continue;
                     }
                     cBoxesNew[k++] = cBoxes[j];
                  }
                  cBoxes = cBoxesNew;
                  
                  
               } 
             
            }
            if (found == true){
               System.out.println("Done");
            } else {
               System.out.println("Not found");
            }
            

            
         }else if (choice == 'l'){
            for(int i = 0; i < counter1; i++){
               System.out.println(cBoxes[i].toString());
            }
            System.out.println("Done");
         } else if (choice == 'q'){
            System.exit(0);
            System.out.println("Done");
         }
     }
      
   }
}