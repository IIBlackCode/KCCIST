package JAVA수업._20200821.TEST02;
import java.util.Scanner;

/*
 * Chapter 05
 * 실행 흐름의 컨트롤
 * Page : 118
 */
public class Test09 {
	public static void main(String[] args) {
		
		@SuppressWarnings("resource")
		Scanner scan = new Scanner(System.in);
		
		System.out.println("스위치문에서 범위로 변수를 입력받기");
		System.out.print("0~100 이내의 자연수를 입력하시오 : ");
		
		int n = scan.nextInt();
		
		switch (n/10) {
		case 0:
			System.out.println("0이상 10 미만 인수");
			System.out.println("조건 : 0 = "+n/10);
			break;
		case 1:
			System.out.println("10이상 20 미만 인수");
			System.out.println("조건 : 1 = "+n/10);
			break;
		case 2:
			System.out.println("20이상 30 미만 인수");
			System.out.println("조건 : 2 = "+n/10);
			break;
		case 3:
			System.out.println("30이상 40 미만 인수");
			System.out.println("조건 : 3 = "+n/10);
			break;
		case 4:
			System.out.println("40이상 50 미만 인수");
			System.out.println("조건 : 4 = "+n/10);
			break;

		default:
			System.out.println("50이상의 자연수");
			System.out.println(n/10);
			break;
		}
	}
}
