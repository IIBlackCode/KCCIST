package com.test;

class Student {
	private String name;

	public void setName(String name) { // Setter
		this.name = name;
	}
	public String getName() { // Getter
		return this.name;
	}
}
public class Test1 {

	public static void main(String[] args) {

		Student stu = new Student();
		stu.setName("ȫ�浿");
		System.out.println(stu.getName());
	}

}
