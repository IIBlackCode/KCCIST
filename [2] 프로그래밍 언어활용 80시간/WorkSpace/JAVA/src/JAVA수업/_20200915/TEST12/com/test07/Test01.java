package JAVA¼ö¾÷._20200915.TEST12.com.test07;

class MyClass {

	@Override
	public String toString() {
		return "MyClass";
	}
	
}

public class Test01 {
	public static void main(String[] args) {
		MyClass c = new MyClass();
		System.out.println(c.toString());
		System.out.println(c);
	}
}
