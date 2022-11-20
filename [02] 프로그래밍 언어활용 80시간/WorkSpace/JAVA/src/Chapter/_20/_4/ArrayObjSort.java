package Chapter._20._4;

import java.lang.reflect.Array;
import java.util.Arrays;

/*
 * 오름차순 정렬
 */

class Person implements Comparable {
	
	private String name;
	private int age;
	
	public Person(String name, int age) {
		super();
		this.name = name;
		this.age = age;
	}

	@Override
	public int compareTo(Object o) {
		Person p = (Person)o;
		System.out.println("compareTo : "+o.toString());
		
		if (this.age > p.age) {
			return 1;
		} else if (this.age < p.age) {
			return -1;
		} else {
			return 0;
		}
	}//the end of method

	@Override
	public String toString() {
		return "Person [name=" + name + ", age=" + age + "]";
	}//the end of method
}//the end of class

public class ArrayObjSort {
	public static void main(String[] args) {
		Person[] ar = new Person[3];
		ar[0] = new Person("Lee", 29);
		ar[1] = new Person("Goo", 15);
		ar[2] = new Person("Soo", 37);
		
		Arrays.sort(ar);
		
		for (Person p : ar) {
			System.out.println(p);
		}
	
	}
}
