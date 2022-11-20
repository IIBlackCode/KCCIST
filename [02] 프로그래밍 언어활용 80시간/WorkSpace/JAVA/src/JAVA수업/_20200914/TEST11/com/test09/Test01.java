package JAVA¼ö¾÷._20200914.TEST11.com.test09;

class MyClass {
	void aMethod() throws ArrayIndexOutOfBoundsException{
		throw new ArrayIndexOutOfBoundsException();
	}
}

public class Test01 {
	public static void main(String[] args) {
		
		MyClass m = new MyClass();
		
		try {
			m.aMethod();
			throw new ArithmeticException();
		} catch (ArrayIndexOutOfBoundsException e) {
			// TODO: handle exception
			System.out.println("Divide by 0");
		}
	}
}
