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
public class Test06 {
	public static void main(String[] args) {
		
		Student student = new Student();
		student.age = 30;
		student.name = "이순신";
		student.gender="남자";
		student.study();
		System.out.println(student.toString());
		
		
		Student student2 = new Student();
		student2.age = 25;
		student2.name = "강감찬";
		student2.gender="남자";
		student2.study();
		System.out.println(student2.toString());
		
		Student s3 = student2;
		System.out.println(s3.toString());
	}//end of main
}//end of class

/*class Student{
	//public 접근제어자 사용시 값을 저장 및 호출이 가능
	public String name;
	public int age;
	public String gender;
	
	public void study() {
		System.out.println(name + ", "+age+", "+gender+" 공부를 한다.");
	}

	@Override
	public String toString() {
		return "Student [name=" + name + ", age=" + age + ", gender=" + gender + "]";
	}
}*/

