package JAVA¼ö¾÷._20200914.TEST11.com.test08;

class MyClass {
	void aMethod() throws ArithmeticException{
		int a = 10/0;
	}
}

public class Test01 {
	
	public static void main(String[] args) {
		MyClass m = new MyClass();

		try {
			m.aMethod();
		} catch (ArithmeticException e) {
			// TODO: handle exception
		}
		
		
	}
	
}
