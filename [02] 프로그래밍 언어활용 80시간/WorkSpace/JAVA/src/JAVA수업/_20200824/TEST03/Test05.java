package JAVA수업._20200824.TEST03;

import java.util.Scanner;

/*
 *	Chapter11
 *	06-1 메소드에 대한 이해와 메소드의 정의
 *	Page : 241
 *
 *	클래스는 변수와 메소드를 함께 묶어서 저장한다.
 */
//클래스 생성시 public이 들어가는 클래스는 독립적인 파일을 생성해야한다.
@SuppressWarnings("unused")
public class Test05 {
	public static void main(String[] args) {
		System.out.println(add(1, 2));
		System.out.println(add(1, 2, 4));
	}
	public static int add(int a, int b) {
		return a+b;
	}
	public static String add1(int a, int b) {
		return "매개변수가 같고 반환타입이 다른 경우 \n 오버로딩이 성립하지 않는다.";
	}
	public static int add(int a, int b, int c) {
		return a+b+c;
	}
}//end of class

