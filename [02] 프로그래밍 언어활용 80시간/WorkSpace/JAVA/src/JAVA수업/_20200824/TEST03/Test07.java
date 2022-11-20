package JAVA수업._20200824.TEST03;

import java.util.Scanner;

/*
 *	Chapter11
 *	11-1 메소드에 대한 이해와 메소드의 정의
 *	Page : 241
 *
 *	클래스는 변수와 메소드를 함께 묶어서 저장한다.
 */

/*
	학생이란 객체를 디자인
	학생의 특징
		1. 나이
		2. 이름
		3. 성별
	학생의 동작, 행위
		1. 공부한다.
 */
@SuppressWarnings("unused")
public class Test07 {
	public static void main(String[] args) {
		int c = 10;
		message(10);
		Student student = new Student();
		student.name = "홍길동";
		student.age = 30;
		student.gender = "남자";
		message2(student);
	}//end of main
	
	public static void message(int count) {
		System.out.println(count);
	}
	public static void message2(Student student2) {
		System.out.println(student2.name);
		student2.study();
	}
	
}//end of class