
public class TestFile{


   public static void main(String [] args){
   
      Register r = new Register();
      Ticket t = new Ticket(new Time("13:00"), "00001");
      String ID_One = t.ID();
      r.add(t);

      Ticket t1 = new Ticket(new Time("13:18"), "00002");
      String ID_Two = t1.ID();
      r.add(t1);
      
      
      
   }
}