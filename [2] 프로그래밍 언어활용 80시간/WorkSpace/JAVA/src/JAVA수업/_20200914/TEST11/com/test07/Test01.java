package JAVA수업._20200914.TEST11.com.test07;

public class Test01 {
	public static void main(String[] args) {
		
		int[] a = new int[5];
//		a[5] = 30/0;//예외발생
		
		try {
			a[5] = 30/0;//예외발생
		} catch (ArithmeticException e) {
			// TODO: handle exception
			System.out.println("By divide 0");
		} catch (ArrayIndexOutOfBoundsException e) {
			// TODO: handle exception
			System.out.println("Array index out of bounds");
		} catch (Exception e) {
			System.out.println("Others exceptions");
		}
		
	}
}
