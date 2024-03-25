import org.junit.Assert;
import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;


public class ShiftTest {


   /** Fixture initialization (common initialization
    *  for all tests). **/
   @Before public void setUp() {
   }


   /** A test that always fails. **/
   @Test public void defaultTest() {
      CalendarTime start = new CalendarTime("1/9/2019%22:00");
      CalendarTime finish = new CalendarTime("2/9/2019%06:00");
      Shift shift = new Shift(start, finish);
      Assert.assertEquals("8 hours", Duration.format(shift.length(), "minute"));
   }
}
