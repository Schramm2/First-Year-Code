import org.junit.Assert;
import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;
import java.util.ArrayList;
import java.util.List;

public class EmployeeTest {


   /** Fixture initialization (common initialization
    *  for all tests). **/
   @Before public void setUp() {
   }


   /** A test that always fails. **/
   @Test public void defaultTest() {
      Employee employee = new Employee("Sivuyile Ngesi", "01010125");
      employee.signIn(new Date(1, 9, 2019), new Time(6,00));
      employee.signOut(new Date(1, 9, 2019), new Time(18,00));
      
      employee.signIn(new Date(2, 9, 2019), new Time(16, 30));
      employee.signOut(new Date(3, 9, 2019), new Time(2, 30));
      
      employee.signIn(new Date(3, 9, 2019), new Time(18,00));
      employee.signOut(new Date(4, 9, 2019), new Time(4,00));
      
      List<Shift> shifts = employee.get(new Date(1, 9, 2019));



      Assert.assertEquals("",Duration.format(employee.hours(new Week(35, 2019)), "minute"));
   }
}
