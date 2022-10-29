package JAVA수업._20200828.TEST10.com.test03;

class A {
	int a;
	static int staticA = 200;
	
	A() {
		a = 100;
	}
	A(int a) {
		this.a = a;
	}
}
class B extends A{
	B() {
		int instanceA = 500;
	}
}

public class Test {
	public static void main(String[] args) {
		System.out.println("상속관계에서 Class변수로 접근");
		System.out.println("A.staticA : "+A.staticA);
		System.out.println("B.staticA : "+B.staticA);
		System.out.println("B b = new B();");
		B b = new B();
		System.out.println("b.a : "+b.a);
	}

}
