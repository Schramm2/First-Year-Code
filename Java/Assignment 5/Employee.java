//Matthew Schramm
//2022/08/30
//Exercise three
//Assignment 5
import java.util.ArrayList;
import java.util.List;

public class Employee{
   public String name;
   public String uid;
   public Shift[] allShifts;
   public int counter;
   public CalendarTime startTime;
   public CalendarTime finishTime;
   
   
   public Employee(String name,String uid){
      this.name = name;
      this.uid = uid;
      this.startTime = startTime;
      this.allShifts = new Shift[100];
      this.finishTime = finishTime;
      this.counter = 0;
      
   }
   public String name(){
   return this.name;
   }
   public String UID(){
      return this.uid;
   }
   public void signIn(Date d, Time t){
      
      CalendarTime tS = new CalendarTime(d, t);
      this.startTime = tS;
      
   }
   public void signOut(Date d, Time t){
      CalendarTime tF = new CalendarTime(d, t);
      this.finishTime = tF;
      allShifts[counter] = new Shift(this.startTime, this.finishTime);
      counter += 1;
      

   }
   public boolean present(){
      
      if(this.startTime != null && this.finishTime == null){
         return true;
      }
      return false;
   }
   public boolean worked(Date d){
      Shift workTime = new Shift(this.startTime,this.finishTime);
      if(workTime.includesDate(d)){
         return true;
         
      }
      return false;
      
      
   }
   public boolean worked(Week w){
      Shift workTime = new Shift(this.startTime,this.finishTime);
      if(workTime.inWeek(w)){
         return true;
         
      }
      return false;
   }
   public List<Shift> get(Date d){
      List<Shift> shifts = new ArrayList<Shift>();
      
      for( int i = 0; i < counter; i++){
         if (worked(d) == true){
            shifts.add(allShifts[i]);
         }
         
      }
      return shifts;
      
      
      
      
      
      
   }
   public List<Shift> get(Week w){
      List<Shift> shifts = new ArrayList<Shift>();
      for( int i = 0; i < counter; i++){
         if (worked(w) == true){
            shifts.add(allShifts[i]);
         }
         
      }
      return shifts;
      

   }
   public Duration hours(Week w){
      Duration sum = null;
      for(int i = 0; i < counter-1; i++){
         sum.add(allShifts[i].length());
      }
      return sum;
   }
}