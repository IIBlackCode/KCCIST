package com.test;

class Employee {
	private String name;

	public void setName(String nm) {
		name = nm;
	}

	public String getName() {
		return name;
	}

	private int age;

	public void setAge(int ag) {
		age = ag;
	}

	public int getAge() {
		return age;
	}

	
}

public class Test1 {
	public static void main(String[] args) {
		Employee emp = new Employee();
		emp.setName("ȫ�浿");
		System.out.println(emp.getName());
		emp.setAge(30);
		System.out.println(emp.getAge());
	}

}