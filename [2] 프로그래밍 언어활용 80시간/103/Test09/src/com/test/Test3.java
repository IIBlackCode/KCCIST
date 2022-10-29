package com.test;

class Student {
	private String name;

	public Student() {
		this("È«±æµ¿");
		this.eat();
	}

	public Student(String name) {
		this.name = name;
	}
	public void study() {
		System.out.println(this.name + "ÀÌ °øºÎÇÏ´Ù.");
	}

	public void eat() {
		System.out.println(this.name + "ÀÌ ¹äÀ» ¸Ô´Ù.");
	}
}

public class Test3 {

	public static void main(String[] args) {
	}

}
