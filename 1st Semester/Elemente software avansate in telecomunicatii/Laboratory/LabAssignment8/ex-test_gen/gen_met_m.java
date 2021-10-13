import java.util.*;

class Member<T> {
 private T id;
 public Member(T id) {
   this.id = id;
 }
 public T getId() {
   return id;
 }
 public void setId(T id) {
   this.id = id;
 }
 
 private static <T> List<T> extractElements(List bag, Class<T> type) {
	 List<T> result = new ArrayList<T>();
	 for(Object e : bag) {
	//if(e instanceof T)  can't use instanceof
	if(type.isAssignableFrom(e.getClass())) {
	    result.add((T) e);
	}
	 }
	 return result;
	}

 public static void main(String[] args) {
   Member<String> mString = new Member<String>("id1");
   mString.setId("id2");
   System.out.printf("id after setting id: %s%n", mString.getId());
   //output:  id after setting id: id2

   Member<Integer> mInteger = new Member<Integer>(1);
   mInteger.setId(2);
   System.out.printf("id after setting id: %d%n", mInteger.getId());
   //output:  id after setting id: 2
   
   List<String> names = new ArrayList<String>();
   names.add("John");
   System.out.printf("List<String> names: %s%n", names);
   /*
    * In the above example, names is a List of String.
    *  When retrieving elements from the List, the return value is
    *   of type String. So no need for casting, which is a big advantage
    *    over the old, non-parameterized collection.
    */
   
   Map<Integer, String> idToName = new HashMap<Integer, String>();
   idToName.put(0, "John");
   System.out.printf("Map<Integer, String> idToName: %s%n", idToName);

   /*
    * In the above example, idToName is a Map with a Integer key and String value. The output is:
Map<Integer, String> idToName: {0=John}

    */
   
	   List<List<String>> listOfList = new ArrayList<List<String>>();
	   List<String> sublist1 = new ArrayList<String>();
	   sublist1.add("A String inside sublist1");
	   listOfList.add(sublist1);

	   List<String> sublist2 = new LinkedList<String>();
	   sublist2.add("A String inside sublist2");
	   listOfList.add(sublist2);
	   System.out.printf("List<List<String>> listOfList: %s%n", listOfList);
	   /*
	   The above example shows a List whose elements are of type List, i.e., a List of List. 
	   The inner List declares that it can only hold String elements. 
	   The first inner list is an ArrayList of String, and the second is a LinkedList of String. 
	   Running this code snippet prints:
	   List<List<String>> listOfList: [[A String inside sublist1], [A String inside sublist2]]

*/
	   
	   List bag = new ArrayList();
	   bag.add(new Integer(0));
	   bag.add(new Integer(1));
	   bag.add(new Double(2008.5));
	   bag.add("a string");
	   List<Number> numbersInBag = extractElements(bag, Number.class);
	   System.out.printf("All elements in bag: %s%nNumber elements in bag: %s%n",
	   bag, numbersInBag);
	   List<Integer> integersInBag = extractElements(bag, Integer.class);
	   System.out.printf("All elements in bag: %s%nInteger elements in bag: %s%n",
	   bag, integersInBag);
/*
 * -------- output -----------
All elements in bag: [0, 1, 2008.5, a string]
Number elements in bag: [0, 1, 2008.5]
All elements in bag: [0, 1, 2008.5, a string]
Integer elements in bag: [0, 1]

 */
 }//main
}//class