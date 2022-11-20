package JAVA수업._20200820.TEST01;

public class PostfixOP {

	public static void main(String[] args) {
		int num = 5;
		System.out.print((num++) + " ");	//	출력 후 값이 증가
		System.out.print((num++) + " ");	//	출력 후 값이 증가
		System.out.print((num) + "\n");	//	출력 후 값이 증가

		System.out.print((num--) + " ");	//	출력 후 값이 증가
		System.out.print((num--) + " ");	//	출력 후 값이 증가
		System.out.print((num) + "\n ");	//	출력 후 값이 증가
	}

}
