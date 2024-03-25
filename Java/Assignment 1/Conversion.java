// CSC1016S assignment 01
// Exercise 1
// Matthew Schramm
// SCHMAT041
// 2022/08/01

// A java program for metric conversion.



public class Conversion{
   // Function definitions
   public Conversion()
   {
   
   }
 
   public double feet2Metres(double feet)
   {
      double metres;
      
      metres = feet/3.2808;
      
      return metres;
   }
   
   public double inches2Cm(double inch)
   {
      double centimetre;
      
      centimetre = inch/0.39370;
      
      return centimetre;
   }
   
   public double feet2Inches(double feet)
   {
      double inches;
      
      inches = feet*12.000;
      return inches;
   }
   
   public double kilometres2Miles(double kilometres)
   {
      double miles;
      
      miles = kilometres*0.6214;
      
      return miles;
   }
   
 }