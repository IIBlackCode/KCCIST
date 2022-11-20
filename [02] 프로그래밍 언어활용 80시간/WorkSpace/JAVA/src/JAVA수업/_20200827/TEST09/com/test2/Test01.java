package JAVA¼ö¾÷._20200827.TEST09.com.test2;


class Animal {
	void eat() {
		System.out.println("Animal eat");
	}
}

class Dog extends Animal {
	void bark() {
		System.out.println("Dog bark");
	}
}

class Cat extends Animal {
	void meow() {
		System.out.println("Cat meow");
		
	}
}

public class Test01 {
	
	static void allEat(Animal a) {

		String className = a.getClass().getSimpleName();
		
		switch (className) {
		case "Dog": 
			Dog d = (Dog) a;
			d.eat();
			d.bark();
			break;
		case "Cat": 
			Cat c = (Cat) a;
			c.eat();
			c.meow();
			break;

		default:
			break;
		}
		
		a.eat();
	}
	
	public static void main(String[] args) {
		Animal a = new Dog();
		Animal a2 = new Cat();
		
		allEat(a);
		allEat(a2);
	}
}
