import org.junit.Assert;
import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;
import java.io.*;
import java.util.*;

public class NumberUtilsTest {


   /** Fixture initialization (common initialization
    *  for all tests). **/
   @Before public void setUp() {
   }


   /** A test that always fails. **/
   @Test public void defaultTest() {
      
      Assert.assertEquals("[9, 9, 9]", Arrays.toString(NumberUtils.toArray(999)));
   }
}
