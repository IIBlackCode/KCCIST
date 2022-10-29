package com.test2;

class A {
	int a;

	A() {
		a = 100;
		System.out.println("Default A Constructor" + a);
		
	}

	A(int a) {
		this.a = a;
		System.out.println("A Constructor " + a);
	}

	class B extends A {
		B() {
			a = 500;
		}
		B(int a){
			super(700);
			this.a = a;
		}
		void bMethod() {
			System.out.println(a);
		}
	}

	}

	public class Test1 {

	public static void main(String[] args) {
		A a = new A();
		A a2 = new A(200);
		B b = new B();
		b.bMethod();
		B b2 = new B(600);
		b2.bMethod();

	}
}
