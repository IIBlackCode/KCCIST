package JAVA수업._20200821.TEST02;

import java.util.Scanner;
/*
 * Chapter 05
 * 실행 흐름의 컨트롤
 * Page : 119
 */
@SuppressWarnings("unused")
public class Test15 {
	public static void main(String[] args) {
		
		for (int i = 0; i < 10; i++) {
			if (i==5) {
				continue; //다시 for문으로 이동
			}
			System.out.println(i);
		}
		
		System.out.println("===");
		
		int j = 1;
		while (j <= 10) {
			if (j==5) {
//				j++;
				continue;
			}
			System.out.println(j);
			j++;
		}
		
	}// the end of main
}// the end of class