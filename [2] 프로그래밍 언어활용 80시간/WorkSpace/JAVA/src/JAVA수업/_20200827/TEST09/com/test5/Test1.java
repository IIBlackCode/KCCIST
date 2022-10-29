package JAVA¼ö¾÷._20200827.TEST09.com.test5;

class A {
	int a;
	A() {
		a = 100;
		System.out.println("Default A Constructor");
	}
	A(int a) {
		this.a = a;
	}
}

class B extends A{
	int b;
	B() {
		System.out.println("Default B Constructor");
	}
	B(int b) {
		super(b*b/(b+b));
		System.out.println("super("+b+")");
		this.b = b;
		System.out.println("B(int b) Constructor, b is "+b);
		System.out.println("[a:"+a+"][b :"+b+"]");
	}
	void bMethod() {
		System.out.println(a);
	}
}

public class Test1 {
	public static void main(String[] args) {
		A a = new A();
		System.out.println("====================");
		B b = new B();
		b.bMethod();
		System.out.println("====================");
		B b2 =new B(500);
		b2.bMethod();
	}
}
