package JAVA수업._20200914.TEST11.com.test06;
/*
 * 예외처리
 */
public class Test01 {
	public static void main(String[] args) {
		int a = 10;
		int b = 0; 
		
		// 에러발생
		int c = a/b;
		
		try {
//		int c = a/b;
		} catch (ArithmeticException e) {
			System.out.println("Exception >> ["+e.getMessage()+"]");
		}
	}
}
