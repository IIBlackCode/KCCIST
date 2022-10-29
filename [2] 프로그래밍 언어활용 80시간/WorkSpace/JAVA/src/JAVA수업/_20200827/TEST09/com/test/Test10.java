package JAVA¼ö¾÷._20200827.TEST09.com.test;

class Animal3 {
	void eat() {
		
	}
}

class Dog3 extends Animal3 {
	void bark() {
		
	}
}

class Cat3 extends Animal3 {
	void meow() {
		
	}
}

public class Test10 {
	static void test(Animal3 a) {
		a.eat();
	}
	
	public static void main(String[] args) {
		Dog3 d = new Dog3();
		d.bark();
		d.eat();
		@SuppressWarnings("unused")
		Animal3 a = d;
		Animal3 a2 = new Dog3();
		a2.eat();
		@SuppressWarnings("unused")
		Animal3 a3 = new Cat3();
		
	}

}
