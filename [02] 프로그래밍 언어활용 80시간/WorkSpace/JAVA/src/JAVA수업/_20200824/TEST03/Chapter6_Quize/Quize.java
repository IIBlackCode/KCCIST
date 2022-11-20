package JAVA수업._20200824.TEST03.Chapter6_Quize;

import java.util.Scanner;

import JAVA수업._20200824.TEST03.Calculator;

class Quize {
	@SuppressWarnings({ "resource", "static-access" })
	public static int quize1(int value1, int value2) {
		System.out.println("********** Quize1 Start **********");
		Calculator calculator = new Calculator();
		
		int result = 0;
		
		while (true) {
			
			@SuppressWarnings("unused")
			Scanner scan = new Scanner(System.in);
			System.out.println("종료시 0");
			System.out.print("[1.+, 2.-, 3.*, 4./]계산방식 선택 : ");
			int choice = scan.nextInt();
			
			if (choice == 1) {
				
//				System.out.print("value1값 입력 :");
//				value1 = scan.nextInt();
//				System.out.print("value2값 입력 :");
//				value2 = scan.nextInt();
				result = calculator.pluse(value1, value2);
				
			} else if (choice == 2) {
				
//				System.out.print("value1값 입력 :");
//				value1 = scan.nextInt();
//				System.out.print("value2값 입력 :");
//				value2 = scan.nextInt();
				result = calculator.minus(value1, value2);
				
			} else if (choice == 3) {
				
//				System.out.print("value1값 입력 :");
//				value1 = scan.nextInt();
//				System.out.print("value2값 입력 :");
//				value2 = scan.nextInt();
				result = calculator.multiply(value1, value2);
				
			} else if (choice == 4) {
				
//				System.out.print("value1값 입력 :");
//				value1 = scan.nextInt();
//				System.out.print("value2값 입력 :");
//				value2 = scan.nextInt();
				result = calculator.divide(value1, value2);
				
			} else {
				break;
			}
		}
		
		return result;
	}//The end of method quize1
	
	@SuppressWarnings("resource")
	public static int quize2(int value1, int value2) {
		System.out.println("********** Quize2 Start **********");
		System.out.println("두 수의 절대값 구하기");
		@SuppressWarnings("unused")
		Scanner scan = new Scanner(System.in);

//		System.out.print("첫 번째 값 입력 : ");
//		int value1 = scan.nextInt();
//		System.out.print("두 번째 값 입력 : ");
//		int value2 = scan.nextInt();
		int result = value1 - value2;
		
		if (result < 0) {
			result = result *(-1);
			System.out.println("절대값 : "+result);
		}else {
			System.out.println("절대값 : "+result);
		}
		return result;
		
	}//The end of method quize2
	
}//The end of class