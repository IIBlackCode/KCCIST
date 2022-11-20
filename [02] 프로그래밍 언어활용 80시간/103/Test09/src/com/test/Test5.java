package com.test;
class Student2{
	String name;
	public void gotoShcool() {
		System.out.println("학생이 학교에 간다.");
	}
	class MiddleStudent2 extends Student2{
		public void study() {
			System.out.println("중학생이 공부하다.");
		}
	}
}
public class Test5 {
	public static void main(String[] args) {
		Student2 stu = new Student2();
		stu.gotoShcool();
		MiddleStudent2 mstu = new MiddleStudent2();
		mstu.gotoSchool();
		mstu.study();
		

	}

