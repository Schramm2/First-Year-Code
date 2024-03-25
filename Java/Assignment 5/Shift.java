//Matthew Schramm
//2022/08/30
//Exercise two
//Assignment 5

public class Shift{
   public CalendarTime start;
   public CalendarTime finish;
   
   public Shift(CalendarTime start, CalendarTime finish){
        this.start = start;
        this.finish = finish;
        
   }
   public CalendarTime start(){
      CalendarTime s = new CalendarTime(start.date(),start.time());
      return s;
   }
   public CalendarTime finish(){
      CalendarTime f = new CalendarTime(finish.date(),finish.time());
      return f;
   }
   public boolean inWeek(Week w){
      boolean fact = false;
      if(w.includes(start.date())== true || w.includes(finish.date())== true ){
         fact = true;
         
      } else{
         fact = false;  
      }
      return fact;
   }
   public boolean includesDate(Date date){
      if (date.compareTo(start.date()) == 0 || date.compareTo(finish.date()) == 0){
         return true;
      }else{
         return false;
      }
   }
   public Duration length(){
      //Time startT = start.time();
      //Time finishT = finish.time();
      Duration length = finish.subtract(start);
      return length;
      
   }
   public String toString(){
      return start.date().toString()+"%"+start.time().toString() +" - "+finish.date().toString()+"%"+finish.time().toString();
   }

   
}