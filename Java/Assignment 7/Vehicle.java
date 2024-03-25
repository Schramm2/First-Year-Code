//Matthew Schramm
//2022/09/27
//Question 2
//Assignment 7

public class Vehicle{
   int cylinders;
   String manufacturer;
   Student owner;
   public Vehicle(int numC, String m, Student o){
      this.cylinders = numC;
      this.manufacturer = m;
      this.owner = o;
      
   }
   public Vehicle(Vehicle v){
      this.cylinders = v.cylinders;
      this.manufacturer = v.manufacturer;
      this.owner = v.owner;
   }
   
   //public String getMaker(){
     // return this.manufacturer;
   //}
   //public int getCylinders(){
     // return this.cylinders;
   //}
   //public String getStudent(){
     // return this.owner.getName();
   //}
   
   
   
   public String toString(){
      return this.manufacturer+", " +this.cylinders+ " cylinders, owned by "+ this.owner.getName() +", a "+ this.owner.getAge() + "-year old "+this.owner.getGender()+" studying "+this.owner.getProgramOfStudy()+ " at "+ this.owner.getNameOfInstitution()+". "+ this.owner.getName()+ " likes "+ this.owner.getHobbies() + ".\n";
   }
}