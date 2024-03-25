import java.util.Scanner;

public class CalculateDuration{
   public static void main(String [] args){
   Scanner input = new Scanner(System.in);
   System.out.println("Enter time A:");
   String t1;
   t1 = input.next();
   Time t2;
   t2 = new Time(t1);
   //System.out.println(t2);
   System.out.println("Enter time B:");
   String t3;
   t3 = input.next();
   Time t4;
   t4 = new Time(t3);
   //System.out.println(t4);
   Duration d1;
   d1 = t4.subtract(t2);
   System.out.println(d1.toString());
   long min = d1.intValue("minute");
   
   System.out.println("The time "+ t4 +" occurs "+min+" minutes after the time " + t2+".");
   }
}
  

   
