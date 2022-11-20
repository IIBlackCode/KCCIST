package JAVA수업._20200827.TEST09.com.test7;

/*
 * Overloading 	:	클래스안의 메소드에 관련된 것.
 * 					이름을 동일하게 쓰고
 * 					파라미터의 개수와 타입에 구별처리 가능하도록 함
 * 
 * Overriding	:	클래스 상속관계, 상위 메소드의 이름을 하위에서 재정의 하는 것
 */

class Animal {
	void eat() {
		System.out.println("Animal eat");
	}
}

class Dog extends Animal{
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
		Dog d = new Dog();
		d.eat();
		Animal a = new Animal();
		a.eat();
		
		Animal a1 =new Dog();
		a1.eat();//재정의한 method가 출력
		Animal a2 =new Cat();
		a2.eat();//재정의한 method가 출력
		
		System.out.println("==============");
		
		/*같은 method를 사용하더라도 다른 출력값이 나온다.*/
		test(new Dog());
		test(new Cat());
	}
}
