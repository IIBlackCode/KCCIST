package JAVA¼ö¾÷._20200827.TEST09.com.test3;
class Animal {}
class Dog extends Animal {}
class Cat extends Animal {}
class BabyDog extends Dog {}
public class Test1 {
	public static void main(String[] args) {
//		Animal a = new Animal();
//		Dog d = (Dog)a;
		
		Dog d = new Dog();
		Animal a = d;
		Cat c = (Cat)a;
	}
}
