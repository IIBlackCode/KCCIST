package JAVA수업._20200828.TEST10.com.test02;

class A {
	int a;
	
	A() {
		a = 100;
		System.out.println("**\ta = 100;\n**\t[A class] Default Constructor [a:"+a+"]");
	}
	A(int a) {
		this.a = a;
		System.out.println("**\tthis.a = a;\n**\t[A class] Overloading Constructor [a:"+a+"]");
	}
}
class B extends A{
	B() {
		System.out.println("**\t[B class] Default Constructor of B class [a:"+a+"]");
		//변수 a는 A class로부터 상속된 변수
		int a = 500;
		System.out.println("**\tint a = 500;\n**\t[B class] Default Constructor of B class [a:"+a+"]");
	}
	B(int a) {
		super(700);
		
		//변수 a는 A class로부터 상속된 변수
		System.out.println("**\tB(int a)\n**\tsuper(700);\n**\t[B class] Default Constructor of B class [a:"+a+"]");
		this.a = a;
		System.out.println("**\tthis.a = a;\n**\t[B class] Default Constructor of B class [a:"+a+"]");
	}

	void bMethod() {
		// TODO Auto-generated method stub
		System.out.println("**\t[The bMethod of B class] "+a);
	}
}

public class Test1 {
	public static void main(String[] args) {
		System.out.println("===========================================================");
		System.out.println("**\tA a = new A();");
		A a = new A();
		System.out.println("===========================================================");
		System.out.println("**\tA a2 = new A(200);");
		A a2 = new A(200);
		System.out.println("===========================================================");
		System.out.println("**\tB b = new B();");
		B b = new B();
		System.out.println("===========================================================");
		System.out.println("**\tb.bMethod();");
		b.bMethod();
		System.out.println("===========================================================");
		System.out.println("**\tB b2 = new B(600);");
		B b2 = new B(600);
		System.out.println("**\tb.bMethod();");
		b2.bMethod();
		System.out.println("===========================================================");
	}
}
