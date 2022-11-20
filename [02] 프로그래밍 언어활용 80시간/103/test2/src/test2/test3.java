package test2;

import java.util.Scanner;

public class test3 {

	public static void main(String[] args) {
//		int choice = 1;
//		if (choice == 1) {
//			System.out.println("짬뽕");
//
//		}
//		if (choice == 2) {
//			System.out.println("자장면");
//
//		}
//		if (choice == 3) {
//			System.out.println("탕수육");
//		}
//
//		if (choice == 1) {
			Scanner sc = new Scanner(System.in);
			System.out.println("메뉴를 선택해주세요. : ");
int choice = sc.nextInt();
if(choice == 1) {
	System.out.println("짬뽕입니다.");
		} else if (choice == 2) {
System.out.println("자장면입니다.");
		} else if (choice == 3) {
			System.out.println("탕수육입니다.");
		} else {
			System.out.println("순번을 다시 확인해주세요.");
		}
	}
}
