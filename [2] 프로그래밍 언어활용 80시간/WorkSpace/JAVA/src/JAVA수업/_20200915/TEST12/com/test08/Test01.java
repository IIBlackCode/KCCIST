package JAVA¼ö¾÷._20200915.TEST12.com.test08;

class Box<T> {
	
	private T ob;
	
	public void set(T o) {
		
	}
	
	public T get() {
		return ob;
	}
	
}

public class Test01 {
	
	static <E> void displayArray(E[] elements) {
		for (E e : elements) {
			System.out.println(e);
		}
	}//The end of method
	
	static <T> void add(T a, T b) {
		
	}
	
	public static void main(String[] args) {

		Box<String> box = new Box();
		Integer[] arr = {10,20,30};
		Test01.<Integer>displayArray(arr);
//		displayArray(arr);
	}
}
