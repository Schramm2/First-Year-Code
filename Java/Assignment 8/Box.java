//Matthew Schramm
//2022/10/11
//Question 1
//Assignment 8
public class Box extends ComputerBox{
   public String colour;
   public int memory;
   
   public Box(String sN, String manu, String c, int mem){
      super(sN,manu);
      this.colour = c;
      this.memory = mem;
   }
   
   public String toString(){
      return "Box: "+super.toString() + this.colour +", "+ this.memory;
   }
}