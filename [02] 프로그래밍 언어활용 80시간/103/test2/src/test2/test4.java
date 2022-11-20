package test2;

import java.util.*;

public class test4 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("나이를 입력해 주세요.");
		int age = sc.nextInt(); // I(아이_대문자)
		if (age > 18) {
			System.out.println("당신은 성인입니다.");
		} else {
			System.out.println("당신은 미성년자입니다.");
		}
		System.out.println("당신의 나이는 " + age);
	}

}
