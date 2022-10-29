package JAVA수업._20200824.TEST03;

import java.util.Scanner;

/*
 *	Chapter 07
 *	07-1 클래스의 정의와 인스턴스의 생성
 *	Page : 157
 *
 *	클래스는 변수와 메소드를 함께 묶어서 저장한다.
 */

@SuppressWarnings("unused")
public class Test09 {
	public static void main(String[] args) {
		message();
		Test09 test09 = new Test09();
		test09.messgae2();
	}//end of main method
	
	public static void message() {
		System.out.println("message");
	}//end of method
	
	public void messgae2() {
		System.out.println("message2");
	}//end of method
	
}//end of class


