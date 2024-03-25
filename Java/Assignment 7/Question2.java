//Matthew Schramm
//2022/09/27
//Question 2
//Assignment 7
import java.util.Scanner;


class Question2{
   public static void main(String [] args){
      Scanner input = new Scanner(System.in);
      
      System.out.println("Enter the vehicle manufacturer: ");//Vehicle
      String vehManu = input.nextLine();
      System.out.println("Enter the name of the vehicle owner: ");//Person
      String ownerName = input.nextLine();
      System.out.println("Enter the owner's gender: ");//Person
      String gender = input.nextLine();
      System.out.println("Enter the owner's programme of study: ");//Student
      String programme = input.nextLine();
      System.out.println("Enter the owner's Institution name: ");//Student
      String insName = input.nextLine();
      System.out.println("Enter the owner's hobbies: ");//Student
      String hobbies = input.nextLine();
      System.out.println("Enter the owner's age: ");//Person
      int age = input.nextInt();
      System.out.println("Enter the number of cylinders in the engine: ");//Vehicle
      int cylinders = input.nextInt();
      System.out.println("Enter the car seating capacity: ");//Car
      int carSeats = input.nextInt();
      System.out.println("Enter the weight of the car: ");//Car
      int carWeight = input.nextInt();
      
      Student carOwner = new Student(ownerName, age, gender, insName, programme, 0, hobbies);
      System.out.println(new Car(cylinders, vehManu, carOwner, carSeats, carWeight));
      
      //System.out.println(car.getMaker()+ ", " + car.getCylinders() + " cylinders, owned by "+ carOwner.getName()  +", a "+ carOwner.getAge() + "-year old "+carOwner.getGender()+ " studying " + carOwner.getProgramme()+
      //" at "+ carOwner.getInstitution() + ". " + carOwner.getName()+ " likes " + carOwner.getHobbies() + ". The car is a "+car.getPassengers() + "-seater weighing " + car.getCarWeight() + " kg.");
      
      
      
      
      
      
      
      
   }
}