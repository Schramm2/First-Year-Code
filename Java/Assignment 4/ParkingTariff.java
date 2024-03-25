// CSC1016S assignment 4
// Exercise 2
// Matthew Schramm
// SCHMAT041
// 2022-08-23

public class ParkingTariff{
   public TimePeriod tp;
   public Money tariff;
   
   public ParkingTariff(TimePeriod tp, Money tariff){
      this.tp = tp;
      this.tariff = tariff;
      
      
      
   }
   public TimePeriod getPeriod(){
      return this.tp;
   }
   public Money getTarriff(){
      return this.tariff;
   }
   public String toString(){
      return this.tp.toString() + " : "+ this.tariff.toString();
   }
   
   
}