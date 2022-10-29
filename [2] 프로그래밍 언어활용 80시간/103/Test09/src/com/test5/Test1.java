package com.test5;
class A {
	int a
	A() {
		a = 100;
		System.out.println("Default A Constructor");
	} 
}
class B extends A {
	B() {
		System.out.println("Default B Constructor");
	}
	B(int b) {
		this.b = b;
		System.out.println(a + "," + b);S
	}
}
void bMethod() {System.out.println(a);}


public class Test1 {

	public static void main(String[] args) {


	}

}
