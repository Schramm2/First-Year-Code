//Matthew Schramm
//2022/10/11
//Question 1
//Assignment 8

public class Rectangle extends VectorObject{
   
   public int xLen;
   public int yLen;
   
   public Rectangle(int id, int x , int y, int xL, int yL){
      super(id, x, y);
      xLen = xL;
      yLen = yL;
   }
   
   public void draw(char[][] matrix){
      boolean steep = Math.abs(yLen-y) > Math.abs(xLen-x);
      if(steep){ 
         x = y;
         xLen = yLen;
      }
      if(x>xLen){
         x = xLen;
         y = yLen;
      }
      int ys;
      if(y < yLen){
         ys = 1;
         
      }else{
         ys = -1;
      }
      int m = Math.abs(yLen - y)/(xLen - x);
      int yA = y;
      int error = 0;
      
      for(int xVar = x; xVar <= xLen; xVar++){
         if (steep){
            setNewCoords(x,y);
            
         }else {
            setNewCoords(y,x);
         }
         error = error +m;
         if (error>0.5){
            y += ys;
            error = error - 1;
         }

      }
      
   }
}