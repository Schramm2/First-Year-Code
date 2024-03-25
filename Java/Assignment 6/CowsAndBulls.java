//Matthew Schramm
//2022/09/23
//Question 2
//Assignment 6
public class CowsAndBulls{
   public final static int NUM_DIGITS = 4;
   public final static int MAX_VALUE = 9876;
   public final static int MIN_VALUE = 1234;
   public final static int MAX_GUESSES = 10;
   public int guessCounter;
   public int mysteryNumber;
   public boolean rightOrWrong;
   
   public CowsAndBulls(int seed){
      // Create a CowsAndBulls game using the given randomisation seed value to generate
      // a mystery number of NUM_DIGITS length, and that gives the player MAX_GUESSES guesses.
      this.mysteryNumber = 0;
      this.guessCounter = MAX_GUESSES;
      this.rightOrWrong = rightOrWrong;
      NumberPicker mysteryNo = new NumberPicker(seed,1, 9);
      for (int i = 0; i <NUM_DIGITS; i++){
         if ( i != 3){
            
            int number = mysteryNo.nextInt();
         
            this.mysteryNumber += number;
            this.mysteryNumber *= 10;

         }else{
            
            int number = mysteryNo.nextInt();
         
            this.mysteryNumber += number;
         }
   }
      
      
      
   }
   public int guessesRemaining(){
      return this.guessCounter;
   }
   public Result guess(int guessNumber){
      
      this.guessCounter -= 1;
      int mysteryNo = this.mysteryNumber;
      int cows = NumberUtils.countIntersect(mysteryNo, guessNumber);
      if (cows == 4){
         this.rightOrWrong = true;
      } else{
         this.rightOrWrong = false;

      }
      int bulls = NumberUtils.countMatches(mysteryNo, guessNumber);
      cows -= bulls;
      Result guessRes = new Result(cows, bulls);
      return guessRes;
      
   }
   public int giveUp(){
      this.rightOrWrong = true;
      return this.mysteryNumber;
   }
   public boolean gameOver(){
      if (this.rightOrWrong == true || this.guessCounter == 0){
         return true;
      } else{
         return false;
      }
   }
}