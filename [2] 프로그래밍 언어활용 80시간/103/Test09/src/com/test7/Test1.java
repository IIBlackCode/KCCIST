// Overloading : 클래스안의 메소드에 관련된 것임. 이름이 동일하게 쓰고
// 파라미터의 개수와 타입에 구별처리 가능하도록 함.
//Overriding: 클래스 상속관계, 상위 메소드 이름을 하위에서 재정의 하는 것.
package com.test7;

class Animal {
	void eat() {
		System.out.println("Animal eat");
	}
}

class Dog extends Animal {
	void eat() {
		System.out.println("Dog eat");
	}
}

class Cat extends Animal {
	void eat() {
		System.out.println("Cat eat");
	}
}

public class Test1 {
	static void test(Animal a) {
		a.eat();
	}

	public static void main(String[] args) {
		test(new Dog());
		test(new Cat());
		Dog d = new Dog();
		d.eat();
		Animal a = new Animal();
		a.eat();
		Animal a1 = new Dog();
		a1.eat();
		Animal a2 = new Cat();
		a2.eat();
	}
}