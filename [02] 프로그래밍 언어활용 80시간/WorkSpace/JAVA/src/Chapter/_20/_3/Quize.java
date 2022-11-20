package Chapter._20._3;

import java.util.Random;
import java.util.Scanner;

/**
 * [난수의 생성]
 * 프로그램 사용자로부터 임의의 정수 A와 Z를 입력받는다.
 * 그리고 A와 Z를 포함하여 그 사이에 있는 난수 10개를 생성하여 
 * 출력하는 프로그램을 작성해보자
 */

public class Quize {
	public static void main(String[] args) {
		//프로그램 사용자로부터 임의의 정수 A와 Z를 입력받는다.
		Scanner scan = new Scanner(System.in);
		
		Random rand = new Random();
		
		System.out.print("임의의 정수A : ");
		String input1 = scan.nextLine();
		System.out.println();
		System.out.print("임의의 정수Z : ");
		String input2 = scan.nextLine();
		
//		System.out.println("큰   수	: "+Integer.max(n1, n2));
//		System.out.println("작은 수	: "+Integer.min(n1, n2));
		
		int min = Integer.min(input1.charAt(0), input2.charAt(0));
		int max = Integer.max(input1.charAt(0), input2.charAt(0));
		
		System.out.println("MIN : "+min+"\nMAX : "+max);
		System.out.println((Integer.compare(min, max)));
		
		for (int i = 0; i < 10; i++) {
			// 0이상 1000미만 난수 생성, 중복있음
			System.out.println((Math.random()*(Integer.compare(min, max))));
		} 
	}
}
