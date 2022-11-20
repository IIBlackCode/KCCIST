package Chapter._34._1;

public class CurrentThreadName {
	public static void main(String[] args) {
		Thread ct = Thread.currentThread();
		String name = ct.getName();
		System.out.println(name);
		
		System.out.println("=============");
	
	}
	
	public static void test() {
		Thread ct = Thread.currentThread();
		String name = ct.getName();
		System.out.println(name);
	}
}
