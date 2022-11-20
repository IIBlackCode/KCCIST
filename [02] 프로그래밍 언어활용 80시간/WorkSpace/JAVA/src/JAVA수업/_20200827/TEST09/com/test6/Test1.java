package JAVA수업._20200827.TEST09.com.test6;

class A {
	int a;
	A() {
		
	}
	A(int a) {
		this.a = a;
	}
}

class B extends A{
	int b;
	B() {
		
	}
	
	B(int b) {
		super(100);
		/*
		 * 1. super(100)가 없으면 부모 클래스의 Default 생성자를 무조건 호출하게 된다. 
		 * 		이 경우 부모클래스에서 Default 생성자가 없으면 오류생김
		 * 2. 생성자의 오버로딩으로 하위 클래스에서 super(100)를 지정해서 부모 클래스(A(int a))를호출하게 되면
		 * 		부모클래스의 Default 생성자를 호출하지 않기 때문에 오류가 생기지 않는다.
		 */
		this.b = b;
	}

}

public class Test1 {
	public static void main(String[] args) {
		B b = new B(100);
		System.out.println(b.a + ", "+b.b);
	}
}
