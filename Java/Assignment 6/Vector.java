//Matthew Schramm
//2022/09/23
//Question 3
//Assignment 6
public class Vector{
   public double x;
   public double y;
   public Vector(double x , double y){
      this.x = x;
      this.y = y;
   }
   public double getX(){
      return this.x;
   }
   public double getY(){
      return this.y;
   }
   public double getMagnitude(){
      double mag = Math.sqrt((Math.pow(this.x,2)+(Math.pow(this.y,2))));
      return mag;
   }
   public Vector add(Vector second){
      double xAdded = this.x + second.getX();
      double yAdded = this.y + second.getY();
      Vector added = new Vector( xAdded, yAdded);
      return added;
   }
   public Vector multiply(double multiple){
      double mX = this.x * multiple;
      double mY = this.y * multiple;
      return new Vector(mX, mY);
   }
   public double dotProduct(Vector two){
      double xMed = this.x * two.getX();
      double yMed = this.y * two.getY();
      double result = xMed + yMed;
      return result;
   }
   public String toString(){
   return "v = ("+String.format("%.2f",this.x)+", "+String.format("%.2f",this.y)+")";
   }
   
}