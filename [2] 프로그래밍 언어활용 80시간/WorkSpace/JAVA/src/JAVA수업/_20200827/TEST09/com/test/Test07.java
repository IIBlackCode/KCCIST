package JAVA수업._20200827.TEST09.com.test;

class A {
	public A() {
		System.out.println("Default A Constructor");
	}
	void aMethod() {
		System.out.println("aMethods");
	}
	@SuppressWarnings("unused")
	private void aPrivateMethod() {
		System.out.println("aMethods");
	}
}//end of class A

class B extends A {
	B() {
		System.out.println("Default B Constructor");
	}
}//end of class B

class C extends B {
	public C() {
		System.out.println("Default C Constructor");
	}
}//end of class C

public class Test07 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		@SuppressWarnings("unused")
		A a = new A();
		B b = new B();
		
		System.out.println("the method Inherited from A class can use in B class");
		b.aMethod();
		System.out.println("상속받더라도 private가 선언된 변수는 접근이 불가능하다.");
//		b.aPrivateMethod();
	}

}
