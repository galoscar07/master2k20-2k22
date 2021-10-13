//Ex1 colectii, generice
import java.util.*;

 class Ex1 {

  private void testCollection() {
    List list = new ArrayList();
    list.add(new String("Hello world!"));
    list.add(new String("Good bye!"));
   // list.add(new Integer(95));
    printCollection(list);
  }

  private void printCollection(Collection c) {
    Iterator i = c.iterator();
   // Iterator <String> i = c.iterator();
    while(i.hasNext()) {
      String item = (String) i.next();
      System.out.println("Item: "+item);
    }
  }

  public static void main(String argv[]) {
    Ex1 e = new Ex1();
    e.testCollection();
  }
}
