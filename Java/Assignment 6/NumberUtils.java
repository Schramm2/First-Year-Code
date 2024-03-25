//Matthew Schramm
//2022/09/23
//Question 1
//Assignment 6
import java.io.*;
import java.util.*;
public class NumberUtils{
   private NumberUtils(){
      
   }
   public static int[] toArray(int number){
      
      int numLength = (String.valueOf(number)).length();
      int[] numbers = new int[numLength];
      for(int i = 0; i<numLength;i++){
          String cDigit = (String.valueOf(number)).substring(i,i+1);
          int digit = Integer.parseInt(cDigit);
          numbers[i] = digit;
           
      } 
      return numbers;
   }
   public static int countMatches(int numberA, int numberB){
      int numLength = (String.valueOf(numberA)).length();
      int counter = 0;
      String letterA = String.valueOf(numberA);
      String letterB = String.valueOf(numberB);
      for(int i = 0; i<numLength; i++){
         if (letterA.charAt(i) == letterB.charAt(i)){
            counter++;
         }
      }
      return counter;
      
   }
   public static int countIntersect(int numberA, int numberB){
      int counter =0;
      int[] aNumbers = new int[100];
      int[] bNumbers = new int[100];
      aNumbers = NumberUtils.toArray(numberA);
      bNumbers = NumberUtils.toArray(numberB);
      for (int i = 0; i < aNumbers.length; i++){
         for (int j = 0; j < bNumbers.length;j++){
            if( aNumbers[i] == bNumbers[j]){
               counter++;
            }
         }
      }
      return counter;

   }
}