package JAVA¼ö¾÷._20200824.TEST03;

public class Test03 {
	public static void main(String[] args) {
		checkEvenOdd(5);
		Test03.checkEvenOdd(4);
	}
	
	public static int checkEvenOdd(int num) {
		if (num % 2 == 0) {
			System.out.println("Evnt");
		}else {
			System.out.println("Odd");
		}
		return num;
	}
	
}//end of class