import org.junit.Assert;
import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;


public class TimePeriodTest {


   /** Fixture initialization (common initialization
    *  for all tests). **/
   @Before public void setUp() {
   }


   /** A test that always fails. **/
   @Test public void defaultTest() {
      final TimePeriod pOne = new TimePeriod(new Duration("hour", 1), new Duration("hour", 2));
      final TimePeriod pTwo = new TimePeriod(new Duration("hour", 2), new Duration("hour", 3));
      final TimePeriod pThree = new TimePeriod(new Duration("hour", 3), new Duration("hour", 4));
      
      
      Assert.assertEquals(true, pOne.precedes(pThree));
   
   
         
   }
}
