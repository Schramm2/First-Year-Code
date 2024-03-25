// CSC1016S assignment 3
// Exercise 2
// Matthew Schramm
// SCHMAT041
// 2022-08-18

public class Ticket{
   public String id;
   public Time issueTime;
  
   
   public Ticket(Time issueTime, String ID){
      this.id = ID;
      this.issueTime = issueTime;
   
   
   }
   public String ID(){
      return this.id;
   
   
   }
   public Duration age(Time currentTime){
      Duration ticketAge = currentTime.subtract(this.issueTime);
      return ticketAge;
   
   }
   public String toString(){
      return "Ticket[id="+this.id +", time="+ this.issueTime.toString()+"]";
   
   
   }
   
   
   
   












}