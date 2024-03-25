//Matthew Schramm
//2022/10/11
//Question 1
//Assignment 8


public class ComputerBox{
   public String serialNo;
   public String manufacturer;
   
   
   public ComputerBox(String sN, String manu){
      this.serialNo = sN;
      this.manufacturer = manu;
      
      
   }
   public String getSerialNo(){
      return this.serialNo;
   }
   public String toString(){
      return this.serialNo + ", "+ this.manufacturer+ ", ";
   }
   
}