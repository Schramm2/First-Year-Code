//Matthew Schramm
//2022/09/27
//Question 2
//Assignment 7

public class Person{
   String name;
   int age;
   String gender;
   
   public Person(String n, int a, String g){
      this.name = n;
      this.age = a;
      this.gender = g;
   }
   public Person(Person p){
      this.name = p.name;
      this.age = p.age;
      this.gender = p.gender;
   }
   public int getAge(){
      return this.age;
   }
   public String getGender(){
      return this.gender;
   }
  
   public String getName(){
      return this.name;
   }
   public void setGender(String newGender){
      this.gender = newGender;
      
   }
   public void setName(String newName){
      this.name = newName;
      
   }
   public void setAge(int newAge){
      this.age = newAge;
      
   }
   
   
   
  
}