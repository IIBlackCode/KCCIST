package test2;

import java.util.Scanner;

public class test18 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (true) {
			System.out.println("######################");
			System.out.println("#1. 구구단 계산 ");
			System.out.println("#2. 종료");
			System.out.print("구구단수를 입력해주세요. :");
			int num = sc.nextInt();
			if (num == 1) {
				System.out.println("단수를 입력해주세요. : ");
				int num2 = sc.nextInt();
				 for (int i = 1; i < 10; i++) {
				 System.out.println(num2 + "x" + i + "=" + (num2 * i));
			
				}
			}else if(num ==2) {
				System.out.println("종료되었습니다.");
				 break;
			}
		}
	}
}
