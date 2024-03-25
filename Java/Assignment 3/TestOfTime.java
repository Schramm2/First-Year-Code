import org.junit.Assert;
import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;


public class TestOfTime {


   /** Fixture initialization (common initialization
    *  for all tests). **/
   @Before public void setUp() {
   }


   /** A test that always fails. **/
   @Test 
   public void testTimeStoring() {
      Time time1 = new Time(17,55,05);
      Assert.assertEquals("17:55:05", time1.toString());
   }
   @Test 
   public void testSubstract  () {
      Time time1 = new Time("17:05:55");
      Time time2 = new Time("13:00:00");
      Duration d = time1.subtract(time2);
      
      Assert.assertEquals(245, d.intValue("minute"));
   }
   @Test 
   public void testSubstractZero  () {
      Time time1 = new Time("17:05:55");
      Duration d = time1.subtract(time1);
      
      Assert.assertEquals(0, d.intValue("minute"));
   }
   @Test 
   public void testDurationMilliSec  () {
      Time time1 = new Time("13:05:55");
      Time time2 = new Time("13:00:00");
      Duration d = time1.subtract(time2);
      
      Assert.assertEquals(355000, d.intValue("millisecond"));
   }
   @Test 
   public void testDurationSecond  () {
      Time time1 = new Time("13:05:55");
      Time time2 = new Time("13:00:00");
      Duration d = time1.subtract(time2);
      
      Assert.assertEquals(355, d.intValue("second"));
   }
   @Test 
   public void testMinute  () {
      Time time1 = new Time("13:05:55");
      Time time2 = new Time("13:00:00");
      Duration d = time1.subtract(time2);
      
      Assert.assertEquals(5, d.intValue("minute"));
   }
   @Test 
   public void testDurationHour  () {
      Time time1 = new Time("17:05:55");
      Time time2 = new Time("13:00:00");
      Duration d = time1.subtract(time2);
      
      Assert.assertEquals(4, d.intValue("hour"));
   }
   


   
   
}
