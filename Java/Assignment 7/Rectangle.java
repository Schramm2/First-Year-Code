//Matthew Schramm
//2022/09/23
//Question 1
//Assignment 7

public class Rectangle extends Shape{
   private double length;
   private double width;
   public Rectangle(String name, String colour, double l, double w){
   
      super(name, colour);
      length = l;
      width = w;
   }
   public Rectangle(Rectangle r){
      super(r);
      this.length = r.length;
      this.width = r.width;
   }
    public String toString(){
      return super.toString()+ " Length " + this.length+ " Width " + this.width;
   }
}