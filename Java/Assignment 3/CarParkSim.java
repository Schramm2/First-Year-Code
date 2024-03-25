// CSC1016S assignment 3
// Exercise 1
// Matthew Schramm
// SCHMAT041
// 2022-08-18
import java.util.Scanner;
/**
 * The CarParkSim class contains the main car park simulation method.
 * It creates and manipulates the main objects, and handles user I/O.
 *
 * @author Stephan Jamieson and ...
 * @version 14/7/2019
 */
public class CarParkSim {
        
    public static void main(final String[] args) {
        final Scanner keyboard = new Scanner(System.in);
        
        // YOUR CODE HERE.
        // Declare variables to store a Clock and a Register object, create the relevant objects and assign them. 
        Clock c = new Clock(new Time("00:00:00"));
        Register r = new Register();
        
        System.out.println("Car Park Simulator");
        
        // YOUR CODE HERE.
        // Print current time.
        Time t = c.examine();
        System.out.println("The current time is "+t.toString()+".");
        
        System.out.println("Commands: advance {minutes}, arrive, depart, quit.");
        System.out.print(">");
        String input = keyboard.next().toLowerCase();
        while (!input.equals("quit")) {
            if (input.equals("advance")) {
                // YOUR CODE HERE.
                // Advance the clock, print the current time.
                int min = keyboard.nextInt();
                Duration minD = new Duration("minute", min);
                c.advance(minD);
                t = c.examine();
                System.out.println("The current time is "+t.toString()+".");
                
                
            }
            else if (input.equals("arrive")) {
            
                // YOUR CODE HERE.
                // Create a new ticket, add it to the register, print details of ticket issued.
                
                String UID =  UIDGenerator.makeUID();
                Ticket tick = new Ticket(c.examine(), UID);
                r.add(tick);
                System.out.println("Ticket issued: "+tick.toString()+".");
                
            }
            else if (input.equals("depart")) {
            
                // YOUR CODE HERE.
                // Determine if ticket is valid, i.e. in the register.
                // If not, print error message.
                // If yes, retreive it, calculate duration of stay and print it.
                
                String ticketID = keyboard.next();
                if (r.contains(ticketID) == true){
                  System.out.println("Ticket details: " + r.retrieve(ticketID).toString() +".");
                  Duration stay = r.retrieve(ticketID).age(c.examine());
                  String length = stay.format(stay,"minute");
                  System.out.println("Duration of stay: " + length + "."); 
                } else{
                  System.out.println("Invalid ticket ID.");

                }
            }
            else {
                System.out.println("That command is not recognised.");
                System.out.println("Commands: advance <minutes>, arrive, depart, quit.");
            }            
            System.out.print(">");
            input = keyboard.next().toLowerCase();
        }            
        System.out.println("Goodbye.");
    }

}
