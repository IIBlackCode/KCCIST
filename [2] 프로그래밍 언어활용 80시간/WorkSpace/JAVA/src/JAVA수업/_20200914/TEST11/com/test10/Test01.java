package JAVA¼ö¾÷._20200914.TEST11.com.test10;

public class Test01 {
	public static void main(String[] args) {
		try {
			int a = 10/0;
		} catch (ArithmeticException e) {
			// TODO: handle exception
			System.out.println(e.getMessage());
		} finally {
			System.out.println("End");
		}
	}
}
