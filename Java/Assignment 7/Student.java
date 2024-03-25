//Matthew Schramm
//2022/09/27
//Question 2
//Assignment 7

public class Student extends Person{
   String nameOfInstitution;
   String programOfStudy;
   int yearOfStudy;
   String hobbies;
   public Student(String name, int age, String gender, String i, String p, int y, String h){
      super(name,age,gender);
      this.nameOfInstitution = i;
      this.programOfStudy = p;
      this.yearOfStudy = y;
      this.hobbies = h;
   
  
   } 
   public Student(Student s){
      super(s);
      this.nameOfInstitution = s.nameOfInstitution;
      this.programOfStudy = s.programOfStudy;
      this.yearOfStudy = s.yearOfStudy;
      this.hobbies = s.hobbies;
   }
   public String getProgramOfStudy(){
      return this.programOfStudy;
   }
   public String getNameOfInstitution(){
      return this.nameOfInstitution;
   }
   public String getHobbies(){
      return this.hobbies;
   }
   public int getYearOfStudy(){
      return this.yearOfStudy;
   }
   public void setNameOfInstitution(String newName){
      this.nameOfInstitution = newName;
   }
   public void setProgramOfStudy(String newProgram){
      this.programOfStudy = newProgram;
   }
   public void setHobbies(String newHobbies){
      this.hobbies = newHobbies;
   }
   public void setYearOfStudy(int newYOS){
      this.yearOfStudy = newYOS;
   }
   
   
   
   
   
}