import java.util.Scanner;
/**
 * Write a description of class CarParkSimSolution here.
 *
 * @author 
 * @version 1
  */
public class CarParkSim {
    
    private CarParkSim() {}
    
    public static void main(final String[] args) {
        final Scanner keyboard = new Scanner(System.in);
        final Clock clock = new Clock(new Time("00:00:00"));
        final Register register = new Register();
        final TariffTable tb = new TariffTable(10);
        System.out.println("Car Park Simulator");
        System.out.printf("The current time is %s.\n", clock.examine());
        System.out.println("Commands: tariffs, advance {minutes}, arrive, depart, quit.");
        System.out.print(">");
        
         final Currency currency = new Currency("R", "ZAR", 100);
         final TimePeriod pOne = new TimePeriod(new Duration("minute", 0), new Duration("minute", 30));
         final TimePeriod pTwo = new TimePeriod(new Duration("minute", 30), new Duration("hour", 1));
         final TimePeriod pThree = new TimePeriod(new Duration("hour",1), new Duration("hour", 3));
         final TimePeriod pFour = new TimePeriod(new Duration("hour", 3), new Duration("hour", 4));
         final TimePeriod pFive = new TimePeriod(new Duration("hour", 4), new Duration("hour", 5));
         final TimePeriod pSix = new TimePeriod(new Duration("hour", 5), new Duration("hour", 6));
         final TimePeriod pSeven = new TimePeriod(new Duration("hour", 6), new Duration("hour", 8));
         final TimePeriod pEight = new TimePeriod(new Duration("hour", 8), new Duration("hour", 10));
         final TimePeriod pNine = new TimePeriod(new Duration("hour", 10), new Duration("hour", 12));
         final TimePeriod pTen = new TimePeriod(new Duration("hour", 12), new Duration("day", 1));

         
         
         tb.addTariff(pOne, new Money("R10", currency));
         tb.addTariff(pTwo, new Money("R15", currency));
         tb.addTariff(pThree, new Money("R20", currency));
         tb.addTariff(pFour, new Money("R30", currency));
         tb.addTariff(pFive, new Money("R40", currency));
         tb.addTariff(pSix, new Money("R50", currency));
         tb.addTariff(pSeven, new Money("R60", currency));
         tb.addTariff(pEight, new Money("R70", currency));
         tb.addTariff(pNine, new Money("R90", currency));
         tb.addTariff(pTen, new Money("R100", currency));
         

        
        String input = keyboard.next().toLowerCase();
        while (!input.equals("quit")) {
            if (input.equals("advance")) {
                clock.advance(new Duration("minute", keyboard.nextInt()));  
                System.out.printf("The current time is %s.\n", clock.examine());
            }
            else if (input.equals("arrive")) {
                final Ticket ticket = new Ticket(clock.examine());
                register.add(ticket);
                System.out.printf("Ticket issued: %s.\n", ticket);
            }
            else if (input.equals("depart")) {
                final String ID = keyboard.next();
                if (!register.contains(ID)) {
                    System.out.println("Invalid ticket ID.");
                }
                else {
                    final Ticket ticket = register.retrieve(ID);
                    System.out.printf("Ticket details: %s.\n", ticket);
                    System.out.printf("Current time: %s.\n", clock.examine());
                    System.out.printf("Duration of stay: %s.\n", ticket.age(clock.examine()).format(ticket.age(clock.examine()),"minute"));
                    System.out.println("Cost of stay : "+ tb.getTariff(ticket.age(clock.examine()))+".");
                }
            } else if (input.equals("tariffs")){
               System.out.println(tb.toString());
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
