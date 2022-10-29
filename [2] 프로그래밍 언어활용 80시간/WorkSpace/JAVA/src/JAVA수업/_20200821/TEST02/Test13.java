package JAVA수업._20200821.TEST02;

import java.util.Scanner;

/*
 * Chapter 05
 * 실행 흐름의 컨트롤
 * Page : 119
 */
public class Test13 {
	public static void main(String[] args) {
		
		Gugudan.gugudanStart();

	}// the end of main
}// the end of class



























class Gugudan {
	
	public Gugudan() {
	}
	
	public static void gugudanStart() {
		@SuppressWarnings("resource")
		Scanner scan = new Scanner(System.in);
		
		
		System.out.println("구구단을 출력하시오.");
		while(true) {
			System.out.print("구구단 버젼을 선택하시오 [1.세로 출력, 2.가로출력, 종료시 다른번호 입력] :");
			int choice = scan.nextInt();
			if (choice == 1) {
				Gugudan.gugudan1();
			}else if(choice == 2) {
				Gugudan.gugudan2();
			}else {
				break;
			}
		}
	}
	public static void gugudan1() {
		System.out.println("[세로출력]");
		for (int i = 2; i <= 9; i++) {
			System.out.println("\n ** " + i + "단 **");
			for (int j = 1; j <= 9; j++) {
				System.out.println(" " + i + " X " + j + " = " + (i * j));
			}
		}
	}
	
	public static void gugudan2() {
		System.out.println("[가로 출력]");
		
		for (int j = 1; j <= 9; j++) {
			for (int i = 2; i <= 9; i++) {
				System.out.print(" " + i + " X " + j + " = " + (i * j) + "\t");
			}
			System.out.println();
		}
		
		System.out.println("2중포문의 위치가 달라진다면");
		
		for (int i = 2; i <= 9; i++) {
			for (int j = 1; j <= 9; j++) {
				System.out.print(" " + i + " X " + j + " = " + (i * j) + "\t");
			}
			System.out.println();
		}
	}
}