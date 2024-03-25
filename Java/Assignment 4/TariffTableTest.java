import org.junit.Assert;
import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;


public class TariffTableTest {


   /** Fixture initialization (common initialization
    *  for all tests). **/
   @Before public void setUp() {
   }


   /** A test that always fails. **/
   @Test public void defaultTest() {
      final Currency currency = new Currency("R", "ZAR", 100);
      final TimePeriod pOne = new TimePeriod(new Duration("hour", 1), new Duration("hour", 2));
      final TimePeriod pTwo = new TimePeriod(new Duration("hour", 2), new Duration("hour", 3));
      final TariffTable tariffTable = new TariffTable(2);
      tariffTable.addTariff(pOne, new Money("R2", currency));
      tariffTable.addTariff(pTwo, new Money("R5", currency));
      
      
      
      
      Assert.assertEquals("", tariffTable.toString());
   }
}
