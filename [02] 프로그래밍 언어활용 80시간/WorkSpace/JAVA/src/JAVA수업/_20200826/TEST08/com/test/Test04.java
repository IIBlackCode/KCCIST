package JAVA¼ö¾÷._20200826.TEST08.com.test;

public class Test04 {
	public static void main(String[] args) {
		A a1 = new A();
		a1.aMethod();
		A a2 = new A();
		a2.aMethod();
		
		B b1 = new B();
		b1.aMethod();
		b1.bMethod();
		System.out.println("=============");
		test1(a1);
		test1(new A());
		System.out.println("=============");
		test1(b1);
		test1(new B());
		System.out.println("=============");
	}
	
	static void test1 (A a) {
		a.aMethod();
	}
	static void test1 (B b) {
		b.bMethod();
	}
}

class A {
	public void aMethod() {
		System.out.println("A Method");
	}
}
class B extends A{
	
	public void bMethod() {
		this.aMethod();
		System.out.println("B Method");
	}
}