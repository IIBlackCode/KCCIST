package test2;

import java.util.Scanner;

public class test7 {

	public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
System.out.println("메뉴를 선택해주세요. : ");
int menu = sc.nextInt();
		switch(menu) {
		case 1:
			System.out.println("짬뽕");
			break;
		case 2:
			System.out.println("자장면");
			break;
		case 3:
			System.out.println("탕수육");
		break;
		default:
	System.out.println("잘못된 메뉴입니다.");
		}
		System.out.println("종료");
	}

}
