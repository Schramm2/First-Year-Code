// CSC1016S assignment 3
// Exercise 3
// Matthew Schramm
// SCHMAT041
// 2022-08-18
public class Register{
   public Ticket[] tickets;
   public int numTickets;
   
   public Register(){
      this.tickets = new Ticket[100];
      this.numTickets = 0;
      
   }
   public void add(Ticket ticket){
      tickets[numTickets] = ticket;
      numTickets += 1;
      
   }
   public boolean contains(String ticketID){
      
      boolean fact = false;
      for (int i = 0; i <= numTickets; i++){
            if ((tickets[i].ID()).equals(ticketID)){
               fact = true;
               return fact;
            }
            
            
            
         
      }
      return fact;
      
      
      
      
      
         
      
      
     
         
   
}
   
   public Ticket retrieve(String ticketID){
      for (int i = 0; i <= numTickets;  i++){
         if ((tickets[i].ID()).equals(ticketID)){
            return tickets[i];
         }
      }
      return tickets[0];
   }

}
