package com.test4;
class A{
	int a;
	A (){a = 100;}
	A(int a) {this.a = a;}
}

class B extends A {
	B(){super(4000);} //super 상속관계에서 내가 원하는 상태를 상위 생성자, 메소드 받고 싶을때 값 호출 방법
	void bMethod() {System.out.println(a); }
}
public class Test1 {
	public static void main(String[] args) {
B b = new B();
b.bMethod();

	}

}
