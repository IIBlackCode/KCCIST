package JAVA수업._20200828.TEST10.com.test05;

class A {
	void testMethod() {
		System.out.println("A");
	}
}

class B extends A{
	void testMethod() {
		System.out.println("A override");
	}
	
}

class C extends B{
//	void testMethod() {
//		System.out.println("A override override");
//	}
}

public class test {
	public static void main(String[] args) {
		A a = new C();
		System.out.println("C 클래스에 있는 override된 testMethod를 주석처리하면?");
		a.testMethod();
		System.out.println("B 클래스에 있는 override된 testMethod가 출력된다.");
	}
}
