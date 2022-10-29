package JAVA¼ö¾÷._20200828.TEST10.com.test07;

class Animal {
	
}
class Dog extends Animal{
	static void testMethod(Animal a) {
		if (a instanceof Dog) {
			Dog d = (Dog)a;
			System.out.println("OK");
		}
	}
}

public class test {
	public static void main(String[] args) {
		Animal a = new Dog();
		Dog.testMethod(a);
		
//		Dog d = (Dog) new Animal();
//		d.testMethod(d);
	}
}
