package com.test5;

class A {
	void testMethod() {
		System.out.println("A");
	}
}

class B extends A {
	void testMethod() {
		System.out.println("A override");
	}
}

class C extends B {
	// void testMethod() {System.out.println("A override override");}
// 슈퍼 클래스의 메서드를 서브 클래스에서 재정의, 서브 클래스에서 재정의 된 메서드가 슈퍼클래스의 메서드보다 우선
}

public class Test1 {
	public static void main(String[] args) {
		A a = new C();
		a.testMethod();
	}

}
