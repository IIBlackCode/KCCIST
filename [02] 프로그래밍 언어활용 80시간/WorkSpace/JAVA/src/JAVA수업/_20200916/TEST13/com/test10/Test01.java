package JAVA수업._20200916.TEST13.com.test10;
/**
 * 
 * 내부 클래스 (inner Class)
 *
 */

abstract class A {
	abstract void aMethod();
}

class B extends A {
	@Override
	void aMethod() {
	}
}

public class Test01 {
	public static void main(String[] args) {
		/*
		 * 일회성 용도로 사용하기 위한 목적
		 */
		A a = new A() {
			
			@Override
			void aMethod() {
				
			}
		};
		
		a.aMethod();
	}
}
