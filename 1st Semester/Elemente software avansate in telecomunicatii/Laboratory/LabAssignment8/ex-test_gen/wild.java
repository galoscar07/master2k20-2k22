import java.util.*;

 class Wild_Ex2 {

  private void testCollection() {
    List<String> list = new ArrayList<String>();
    list.add(new String("Hello world!"));
    list.add(new String("Good bye!"));
    //list.add(new Integer(95));
    printCollection(list);
  }

  /*
   * private void printCollection(Collection c) {

    Iterator<String> i = c.iterator();
    while(i.hasNext()) {
      System.out.println("Item: "+i.next());
    }
  }

  public void printCollection(Collection c) {
	   Iterator i = c.iterator();
	   for(int k = 0;k<c.size();k++) {
	     System.out.println(i.next());
	   }
	  }
	   */
  
  void printCollection(Collection<?> c) {
	   for(Object o:c) {
	      System.out.println(o);
	   }
	}


  public static void main(String argv[]) {
    Wild_Ex2 e = new Wild_Ex2();
    e.testCollection();
  }
}
