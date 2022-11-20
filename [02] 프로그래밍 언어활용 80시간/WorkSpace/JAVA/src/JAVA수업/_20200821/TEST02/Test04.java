package JAVA수업._20200821.TEST02;
import java.util.Scanner;

/*
 * Chapter 05
 * 실행 흐름의 컨트롤
 * 104Page
 */
public class Test04 {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		@SuppressWarnings("resource")
		Scanner scan = new Scanner(System.in);
		System.out.print("나이를 입력하시오 : ");
		int age = scan.nextInt();
		
		if (age > 18) {
			System.out.println("당신은 성인입니다.");
		}else {
			System.out.println("당신은 미성년자입니다.");
		}
		System.out.println("당신의 나이는 : "+age+"입니다.");
		
		System.out.print("메뉴를 선택 해 주세요\n1.짬뽕, 2.짜장면, 3.탕수육\n선택 : ");
		int choice = scan.nextInt();
		if (choice == 1) {
			System.out.println("짬뽕을 선택하셧습니다.");
		} else if (choice == 2) {
			System.out.println("짜장면을 선택하셧습니다.");
		} else if (choice == 3) {
			System.out.println("탕수육을 선택하셧습니다.");
		} else {
			System.out.println("잘못 고르셧습니다.");
		}
		
	}
}
