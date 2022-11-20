package JAVA수업._20200824.TEST03.Chapter6_Quize;

import java.util.Scanner;

public class Chapter06_1 {

	@SuppressWarnings("static-access")
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		@SuppressWarnings("resource")
		Scanner scan = new Scanner(System.in);
		Quize qzuize = new Quize();
		int choice = 0;
		
		while (true) {
			System.out.print("다음 게임 진행시 1번을 눌러주세요 :");
			choice = scan.nextInt();
			if (choice == 1) {
				System.out.print("value1값 입력 :");
				int value1 = scan.nextInt();
				System.out.print("value2값 입력 :");
				int value2 = scan.nextInt();
				
				qzuize.quize1(value1, value2);
				qzuize.quize2(value1, value2);
			}else {
				break;
			}//end of if
			
		}//end of while
		
	}//end of main Method

}//The end of Class