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
 public static void main(String[] args) {
   Member<String> mString = new Member<String>("id1");
   mString.setId("id2");
   System.out.printf("id after setting id: %s%n", mString.getId());
   //output:  id after setting id: id2

   Member<Integer> mInteger = new Member<Integer>(1);
   mInteger.setId(2);
   System.out.printf("id after setting id: %d%n", mInteger.getId());
   //output:  id after setting id: 2
 }
}