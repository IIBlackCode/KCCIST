package JAVA수업._20200915.TEST12.com.test04;

import java.lang.reflect.Array;
import java.util.Arrays;

/*
 * 오름차순 정렬
 */

class Student implements Comparable {
	
	private int rollno;
	private String name;
	private int age;
	
	public Student(int rollno,String name, int age) {
		super();
		this.rollno = rollno;
		this.name = name;
		this.age = age;
	}
	
	//Sorting 기준을 정하기 위해 compareTo를 구현한다
	@Override
	public int compareTo(Object o) {
		Student p = (Student)o;
		System.out.println("compareTo : "+o.toString());
		
		if (this.rollno > p.rollno) {
			return 1;
		} else if (this.rollno < p.rollno) {
			return -1;
		} else {
			return 0;
		}
	}//the end of method

	@Override
	public String toString() {
		return "Student [rollno=" + rollno + ", name=" + name + ", age=" + age + "]";
	}
	
}//the end of class

public class Test01 {
	public static void main(String[] args) {
		
		Student[] ar = new Student[3];
		ar[0] = new Student(1111,"이순신", 29);
		ar[1] = new Student(2222,"홍길동", 15);
		ar[2] = new Student(3333,"강감찬", 37);
		
		Arrays.sort(ar);
		System.out.println("정렬결과");
		for (Student p : ar) {
			System.out.println(p);
		}
	
	}//The end of Main Method
}//The end of class