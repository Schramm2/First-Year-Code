//Matthew Schramm
//2022/10/11
//Question 1
//Assignment 8

public class HLine extends VectorObject{
   public int length;
   public HLine(int id, int x , int y, int l){
      super(id, x, y);
      length = l;
   }
   public void draw(char[][] matrix){
      boolean steep = Math.abs(bY-y) > Math.abs(bX-x);
      if(steep){ 
         x = y;
         bX = bY;
      }
      if(x>bX){
         x = bX;
         y = bY;
      }
      int ys;
      if(y < bY){
         ys = 1;
         
      }else{
         ys = -1;
      }
      int m = Math.abs(bY - y)/(bX - x);
      int yA = y;
      double error = 0;
      
      for(int xVar = x; xVar <= bX; xVar++){
         if (steep){
            setNewCoords(x,y);
            
         } else{  
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