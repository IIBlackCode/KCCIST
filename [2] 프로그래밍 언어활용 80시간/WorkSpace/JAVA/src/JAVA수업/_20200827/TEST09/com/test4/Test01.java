package JAVA수업._20200827.TEST09.com.test4;
class A {
	int a;
	A() {
		a = 100;
	}
	
	A(int a) {
		this.a = a;
		System.out.println("The Constructor of Class A ");
	}
}

class B extends A {
	public B() {
//		a = 1000;
		super(4000); // 부모클래스의 생성자 호출
	}
	void bMethod() {
		System.out.println(a);
	}
}

public class Test01 {
	public static void main(String[] args) {
		B b = new B();
		b.bMethod();
	}
}
