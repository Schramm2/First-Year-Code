import org.junit.Assert;
import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;


public class TicketTest {


   /** Fixture initialization (common initialization
    *  for all tests). **/
   @Before public void setUp() {
   }


   /** A test that always fails. **/
   @Test public void defaultTest() {
      Time tOne = new Time("6:50");
      Ticket ticket = new Ticket(tOne, "8005A3");
      Time tTwo = new Time("7:19");
      Duration d = ticket.age(tTwo);
      Assert.assertEquals(29, d.intValue("minute"));
   }
}
