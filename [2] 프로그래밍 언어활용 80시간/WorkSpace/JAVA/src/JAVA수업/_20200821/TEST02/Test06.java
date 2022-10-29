package JAVA수업._20200821.TEST02;
import java.util.Scanner;

/*
 * Chapter 05
 * 실행 흐름의 컨트롤
 * Page : 111
 */
public class Test06 {
	public static void main(String[] args) {
		
		@SuppressWarnings("resource")
		Scanner scan = new Scanner(System.in);
		System.out.print("나이를 입력하시오 : ");
		
		int age = scan.nextInt();
		
		String msg = (age > 18) ? "성인":"미성년자";
		System.out.println(msg);
	}
}
