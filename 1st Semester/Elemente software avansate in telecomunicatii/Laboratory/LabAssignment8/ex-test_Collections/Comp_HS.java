// Use a custom comparator.
import java.util.*;
// A reverse comparator for strings.
class MyComp implements Comparator {
public int compare(Object a, Object b) {
String aStr, bStr;
aStr = (String) a;
bStr = (String) b;
// reverse the comparison
return bStr.compareTo(aStr);
}
// no need to override equals
}
class CompDemo {
public static void main(String args[]) {
// Create a tree set
TreeSet ts = new TreeSet(new MyComp());
// Add elements to the tree set
ts.add("C");
ts.add("A");
ts.add("B");
ts.add("E");
ts.add("F");
ts.add("D");
// Get an iterator
Iterator i = ts.iterator();
// Display elements
while(i.hasNext()) {
Object element = i.next();
System.out.print(element + " ");
}
System.out.println();
}
}
