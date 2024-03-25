t//Matthew Schramm
//2022/10/11
//Question 1
//Assignment 8
public class Accessory extends ComputerBox{
   public String colour;
   
   
   public Accessory(String sN, String manu, String c){
      super(sN,manu);
      this.colour = c;
     
   }
   public String toString(){
      return "Accessories: "+super.toString() + this.colour ;
   }
}