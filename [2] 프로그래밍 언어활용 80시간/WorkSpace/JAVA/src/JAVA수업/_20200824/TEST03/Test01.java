package JAVA수업._20200824.TEST03;

/*
 *	Chapter6 
 *	06-1 메소드에 대한 이해와 메소드의 정의
 *	Page : 138
 *
 *	클래스는 변수와 메소드를 함께 묶어서 저장한다.
 */
public class Test01 { 
	public static void main(String[] args) {
		
		int x = 1;
		int y = 2;
		int z = add(x, y);
		
		System.out.println(z);
		
	}//The end of main method
	
	public static int add(int a, int b) {
		
		int c = a + b;
		return c;
		
	}
	
}//The end of class
