package JAVA수업._20200828.TEST10.com.test06;
class A {
	
}
class B extends A{
	
}

public class test {

	public static void main(String[] args) {
		/*
		 * instanceof : 객체비교시 상속관계면 true를 반환, 형변환 가능
		 */
		A a = new A();
		System.out.println(a instanceof A);
		B b = new B();
		System.out.println(b instanceof A);
		B b2 = null;
		System.out.println(b2 instanceof A);
		
	}

}
