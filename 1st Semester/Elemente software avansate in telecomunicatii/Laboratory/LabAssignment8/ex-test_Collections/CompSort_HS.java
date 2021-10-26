// Use a comparator to sort accounts by last name.
import java.util.*;

// Compare last whole words in two strings.
class TComp implements Comparator {
public int compare(Object a, Object b) {
int i, j, k;
String aStr, bStr;
 
aStr = (String) a;
bStr = (String) b;
// find index of beginning of last name
i = aStr.lastIndexOf(' ');
j = bStr.lastIndexOf(' ');
k = aStr.substring(i).compareTo(bStr.substring(j));
if(k==0) // last names match, check entire name
return aStr.compareTo(bStr);
else
return k;
}
// no need to override equals
}
class TreeMapDemo2 {
public static void main(String args[]) {
// Create a tree map
TreeMap tm = new TreeMap(new TComp());
// Put elements to the map
tm.put("John Doe", new Double(3434.34));
tm.put("Tom Smith", new Double(123.22));
tm.put("Jane Baker", new Double(1378.00));
tm.put("Todd Hall", new Double(99.22));
tm.put("Ralph Smith", new Double(-19.08));
// Get a set of the entries
Set set = tm.entrySet();
// Get an iterator
Iterator itr = set.iterator();
// Display elements
while(itr.hasNext()) {
Map.Entry me = (Map.Entry)itr.next();
System.out.print(me.getKey() + ": ");
System.out.println(me.getValue());
}
System.out.println(); 
// Deposit 1000 into John Doe's account
double balance = ((Double)tm.get("John Doe")).doubleValue();
tm.put("John Doe", new Double(balance + 1000));
System.out.println("John Doe's new balance: " +
tm.get("John Doe"));
}
}
