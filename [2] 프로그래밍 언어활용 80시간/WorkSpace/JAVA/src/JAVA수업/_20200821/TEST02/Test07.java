package JAVA수업._20200821.TEST02;
import java.util.Scanner;

/*
 * Chapter 05
 * 실행 흐름의 컨트롤
 * Page : 117
 */
public class Test07 {
	public static void main(String[] args) {
		
		@SuppressWarnings("resource")
		Scanner scan = new Scanner(System.in);
		System.out.print("메뉴를 선택 해 주세요\n1.짬뽕, 2.짜장면, 3.탕수육\n선택 : ");
		int choice = scan.nextInt();
		/*
		if (choice == 1) {
			System.out.println("짬뽕을 선택하셧습니다.");
		} else if (choice == 2) {
			System.out.println("짜장면을 선택하셧습니다.");
		} else if (choice == 3) {
			System.out.println("탕수육을 선택하셧습니다.");
		} else {
			System.out.println("잘못 고르셧습니다.");
		}
		 */
		
		switch (choice) {
		case 1: System.out.println("짬뽕을 선택하셧습니다.");
			break;
		case 2: System.out.println("짜장면을 선택하셧습니다.");
			break;
		case 3: System.out.println("탕수육을 선택하셧습니다.");
			break;

		default: System.out.println("잘못 고르셧습니다.");
			break;
		}
	}
}
