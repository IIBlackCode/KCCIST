package JAVA수업._20200821.TEST02;

import java.util.Scanner;

/*
 * Chapter 05
 * 실행 흐름의 컨트롤
 * Page : 119
 */
public class Test11 {
	public static void main(String[] args) {

		@SuppressWarnings("resource")
		Scanner scan = new Scanner(System.in);
		
		System.out.println("while문을 이용한 무란루프");
		
		while (true) { //조건이 true일 때 로직 무한반복
			System.out.print("Please choise the menu : ");
			int menu = scan.nextInt();

			if (menu == 1) {
				System.out.println("짬뽕");
			} else {
				break;
			}// the end of if
		}// the end of while
		System.out.println("종료되었습니다.");
	}//the end of main
}//the end of class
