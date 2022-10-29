package JAVA수업._20200821.TEST02;

import java.util.Scanner;

public class Quize {
	/*
	1. 사용자가 입력한 구구단을 출력하시오.
	출력결과 
	원하는 구구단수를 입력하시오. : 2
	
	2 x 1 = 2
	2 x 2 = 4
	..
	 */
	
	public static void manual() {
		System.out.println("****************************  각 구문의 무한루프  *******************************");
		System.out.println("=================================================================================");
		System.out.println("\n\twhile(true) {\n\t	System.out.println(\"test\");\n\t}\n\n\tfor (;;) {\n\t	System.out.println(\"test\");\n\t}\n\n");
		System.out.println("=================================================================================");
	}
	public static void quize1() {
		
		@SuppressWarnings("resource")
		Scanner scan = new Scanner(System.in);
		
		System.out.println("1. 사용자가 입력한 구구단을 출력하시오.");
		System.out.print("원하는 구구단수를 입력하시오. :");
		int dan = scan.nextInt();
		
		for (int j = 1; j <10; j++) {
			System.out.println(" " + dan + " X " + j + " = " + (dan * j));
		}
		
		System.out.println("\n\n");
	}// The end of method quize1
	
	public static void quize2() {
		System.out.println("2. 다음의 결과를 출력하시오.");
		for (int i = 1; i <= 5; i++) {
			for (int j = 1; j <= 5; j++) {
				if (j<=i) {
					System.out.print("*");
//					System.out.print(" ["+i+"]["+j+"]  ");
//					System.out.print(" ["+i+"]["+j+"]  ");
				}
			}
			System.out.println();
		}
		System.out.println("-----------");
		for (int i = 1; i <= 5; i++) {
			for (int j = 1; j <= i; j++) {
//					System.out.print("*");
					System.out.print(" ["+i+"]["+j+"]  ");
			}
			System.out.println();
		}
		System.out.println("\n\n");
	}// The end of method quize2
	
	
	public static void quize3() {
		System.out.println("3. 다음의 결과를 출력하시오.");
		System.out.println("조건문 방식");
		for (int i = 1; i <= 9; i++) {
			for (int j = 1; j <= 9; j++) {
				if (j+i<=10) {
//					System.out.print("*");
//					System.out.print(" ["+i+"]["+j+"]  ");
//					System.out.print(" ["+j+"]  ");
					System.out.print(" "+ j+" " );
				}
			}
			System.out.println();
		}
		System.out.println("-----------------------");
		System.out.println("for문 수정방식 1");
		for (int i = 1; i <= 9; i++) {
			for (int j = 1; j <= 10-i; j++) {

				System.out.print(" "+ j+" " );
			}
			System.out.println();
		}
		System.out.println("-----------------------");
		System.out.println("for문 수정방식 2");
		for (int i = 9; i >= 1; i--) {
			for (int j = 1; j <= i; j++) {
				
				System.out.print(" "+ j+" " );
			}
			System.out.println();
		}
		
		
		System.out.println("\n\n");
	}// The end of method quize3
}
