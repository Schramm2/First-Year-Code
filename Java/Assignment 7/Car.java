//Matthew Schramm
//2022/09/27
//Question 2
//Assignment 7

public class Car extends Vehicle{
   int capacity;
   double weight;
   public Car(int numCylinders, String maker, Student owner, int cap, double carW){
      super(numCylinders, maker, owner);
      this.capacity = cap;
      this.weight = carW;
   }
   public Car(Car c ){
      super(c);
      this.capacity = c.capacity;
      this.weight = c.weight;
      
   }
   
   @Override

   public String toString(){
      return super.toString() + "The car is a " + this.capacity +"-seater weighing " + this.weight + " kg";
   }
}