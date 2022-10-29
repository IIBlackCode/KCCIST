package JAVA수업._20200821.TEST02;
import java.util.Scanner;

/*
 * Chapter 05
 * 실행 흐름의 컨트롤
 * Page : 117
 */
public class Test08 {
	public static void main(String[] args) {
		
		@SuppressWarnings("resource")
		Scanner scan = new Scanner(System.in);

		System.out.print("나이를 입력 해 주세요 : ");
		int world1 = scan.nextInt();
		
		System.out.println();
		
		System.out.print("이름을 입력 해 주세요 : ");
		String world2 = scan.next();
		
		System.out.println("나이 : "+world1 + " 이름 : "+world2);
	}
}
