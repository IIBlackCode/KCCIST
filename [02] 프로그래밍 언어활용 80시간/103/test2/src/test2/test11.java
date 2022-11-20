package test2;

import java.util.Scanner;

public class test11 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (true) {
			System.out.print("메뉴를 입력해주세요. :");
			int menu = sc.nextInt();
			if (menu == 1) {
				System.out.println("짬뽕");
			} else {
				break;
			}
		}
		System.out.println("종료되었습니다.");
	}
}
