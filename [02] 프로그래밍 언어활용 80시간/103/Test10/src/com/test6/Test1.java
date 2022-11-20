package com.test6;

class A {
}

class B extends A {
}

public class Test1 {
	public static void main(String[] args) {
		A a = new A();
		System.out.println(a instanceof A);
		B b = new B();
		System.out.println(b instanceof A);
		B b2 = null;
		System.out.println(b2 instanceof A);
//		B b3 = new A();
	}

}
