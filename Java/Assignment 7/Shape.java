//Matthew Schramm
//2022/09/23
//Question 1
//Assignment 7

public class Shape{
   private String name;
   private String colour;
   
   public Shape(Shape s){
      this.name = s.name;
      this.colour = s.colour;
   }
   public Shape (String n, String c){
      this.name = n;
      this.colour = c;
      
   }
   public String toString(){
      return this.name+ " " + this.colour;
   }
   
   
}