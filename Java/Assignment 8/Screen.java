//Matthew Schramm
//2022/10/11
//Question 1
//Assignment 8
public class Screen extends ComputerBox{
   public String colour;
   public int size;
   
   public Screen(String sN, String manu, String c, int s){
      super(sN,manu);
      this.colour = c;
      this.size = s;
   }
   public String toString(){
      return "Screen: "+super.toString() + this.colour +", "+ this.size;
   }
}