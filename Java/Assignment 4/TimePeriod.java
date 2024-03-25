// CSC1016S assignment 4
// Exercise 1
// Matthew Schramm
// SCHMAT041
// 2022-08-23
public class TimePeriod{
   private Duration lowerBound;
   private Duration upperBound;

   public TimePeriod(Duration lowerBound, Duration upperBound){
      this.lowerBound = lowerBound;
      this.upperBound = upperBound;
   }
   public Duration lowerBound(){
      return this.lowerBound;
   }
   public Duration upperBound(){
      return this.upperBound;
      
   }
   public boolean includes(Duration duration){
      boolean fact = false;
      if ((duration.compareTo(lowerBound) > 0 || duration.compareTo(lowerBound) == 0) && (duration.compareTo(upperBound)) < 0){
         fact = true;
      }else{
         fact = false;
      }
      return fact;
   }
   public boolean precedes(TimePeriod other){
      boolean fact = false;
      if((this.upperBound().compareTo(other.lowerBound) < 0) || (this.upperBound().compareTo(other.lowerBound) == 0)){
         fact = true;
      } else{
         fact = false;
      }
      return fact;
   }
   public boolean adjacent(TimePeriod other){
      boolean fact = false;
      if((this.upperBound().compareTo(other.lowerBound()) == 0) || (this.lowerBound().compareTo(other.upperBound()) == 0)){
         fact = true;
      } else{
         fact = false;
      }
      return fact;
   }
   public String toString(){
      return "["+((this.lowerBound().format(this.lowerBound(),"hour","minute")) + " .. "+ (this.upperBound().format(this.upperBound(),"hour","minute"))+"]");
   }
   

   

}