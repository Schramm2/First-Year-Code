import org.junit.Assert;
import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;


public class RegisterTest {


   /** Fixture initialization (common initialization
    *  for all tests). **/
   @Before public void setUp() {
   }


   /** A test that always fails. **/
   @Test 
   public void defaultTest() {
      Register r = new Register();
      Ticket t = new Ticket(new Time("13:00"), "00001");
      String ID_One = t.ID();
      r.add(t);

      t = new Ticket(new Time("13:18"), "00002");
      String ID_Two = t.ID();
      r.add(t);
      t = new Ticket(new Time("13:50"), "00003");
      String ID_Three = t.ID();
      r.add(t);
      String ID_Four = "00004";
     

      Assert.assertEquals(true, r.contains(ID_Two));
   }
}
