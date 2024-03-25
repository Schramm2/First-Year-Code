// CSC1016S assignment 4
// Exercise 2
// Matthew Schramm
// SCHMAT041
// 2022-08-23

public class TariffTable{
   public int maxSize;
   public ParkingTariff[] parkT;
   public int countTariffs;
   
   
   public TariffTable(int maxSize){
      this.maxSize = maxSize;
      this.parkT = new ParkingTariff[maxSize];
      this.countTariffs = 0;
      
      
   }
   
   public void addTariff(TimePeriod period, Money tariff){
      if (countTariffs == 0){
        ParkingTariff pt = new ParkingTariff(period, tariff);
        parkT[countTariffs] = pt;
        countTariffs += 1;
      } else if (countTariffs < maxSize){
         if( ((parkT[countTariffs-1].getPeriod()).precedes(period) == true) && ((parkT[countTariffs-1].getPeriod()).adjacent(period) == true) ){
            ParkingTariff pt = new ParkingTariff(period, tariff);
            
            parkT[countTariffs] = pt;
            countTariffs += 1;
         } else {
            throw new IllegalArgumentException("Tariff periods must be adjacent.");
         }
      }
      
      
      
      
   }
   public Money getTariff(Duration lengthOfStay){
      for(int i = 0; i < countTariffs; i++){
         if((parkT[i].getPeriod()).includes(lengthOfStay) == true ){
            return parkT[i].getTarriff();
         } 
      }
      return parkT[0].getTarriff();
         
   }
   public String toString(){
      String output = "";
      for(int i = 0; i < countTariffs; i++){
         if (i != countTariffs -1){
            output += parkT[i].toString() + "\n";
         }else{
            output += parkT[i].toString();

         }
         
      }
      return output;
      
   }
}