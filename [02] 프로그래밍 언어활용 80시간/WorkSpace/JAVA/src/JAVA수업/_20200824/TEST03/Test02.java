package JAVA¼ö¾÷._20200824.TEST03;

public class Test02 {
	/*Indicates that the named compiler warnings should be suppressed in theannotated element */
	@SuppressWarnings("static-access")
	public static void main(String[] args) {
		int x = Calculator.pluse(1, 2);
		System.out.println(x);
		
		int y = add1(1, 2);
		System.out.println(y);
		add2(1, 2);
		
		TestClass tc = new TestClass();
		tc.iv = 0;
		tc.cv = 0;
		
		TestClass.cv = 0;
	}
	
	public static int add1(int a , int b) {
		System.out.println("add1 Method");
		return a + b;
	}
	public static int add2(int a , int b) {
		System.out.println("add2 Method");
		System.out.println(a+b);
		return a + b;
	}
}

class TestClass {
	int iv;
	static int cv;
	
	void instanceMethod() {
		System.out.println(iv);
		System.out.println(cv);
	}
	
	static void staticMethod() {
//		System.out.println(iv);
		System.out.println(cv);
	}
}
