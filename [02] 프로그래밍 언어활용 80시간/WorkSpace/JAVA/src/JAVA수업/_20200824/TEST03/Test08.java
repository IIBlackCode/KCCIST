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
	강아지
	학생의 특징
		1. 색깔
		2. 크기
		3. 종
	학생의 동작, 행위
		1. 짖는다, 먹는다, 달린다
 */
@SuppressWarnings("unused")
public class Test08 {
	public static void main(String[] args) {
		Dog dog = new Dog();
		dog.color = "검은색";
		dog.size = 140;
		dog.species = "";
	}
	
}//end of class








/*
강아지
학생의 특징
	1. 색깔
	2. 크기
	3. 종
학생의 동작, 행위
	1. 짖는다, 먹는다, 달린다
*/
class Dog {
	//member variables
	public String color;
	public int size;
	public String species;
	
	//member methods
	public void bark() {
		System.out.println("개가 짖는다.");
	}
	public void eat() {
		System.out.println("먹는다.");
	}
	public void run() {
		System.out.println("달린다");
	}
	public void display() {
		System.out.println(color+", "+size+", "+species);
	}
}