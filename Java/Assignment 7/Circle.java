//Matthew Schramm
//2022/09/23
//Question 1
//Assignment 7

public class Circle extends Shape{
   private double radius;
   
   public Circle(String name, String colour, double r){
      super(name, colour);
      radius = r;
      
      
   }
   public Circle(Circle c){
      super(c);
      this.radius = c.radius;
   }
   
   
    public String toString(){
      return super.toString()+  " Radius " + this.radius;
   }
}