package com.test8;

class Man {
	String name;

	public Man(String name) {
		this.name = name;
	}

	public void tellYourName() {
		System.out.println("My name is " + name);
	}
}

class BusinessMan extends Man { //Man을 상속하는 BusinessMan
	String company;
	String position;

	public BusinessMan(String name, String company, String position) {
		super(name);
		this.company = company;
		this.position = position;
	}

	public void tellYourInfo() {
		System.out.println("My company is " + company);
		System.out.println("My Position is " + position);
		tellYourName(); // Man 클래스를 상속했기 때문에 호출 가능!
	}
}

class MyBusinessMan2 {
	public static void main(String[] args) {
		BusinessMan man = new BusinessMan("YOON", "Hybrid ELD", "Staff Eng.");
		man.tellYourInfo();
	}
}
