package JAVA¼ö¾÷._20200826.TEST08.com.test;

public class Test03 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Animal a = new Animal();
		a.breath();
		
		Dog dog = new Dog();
		dog.breath();
	}

}

class Animal{
	public void breath() {
		System.out.println("Animal breath");
	}
}

class Dog extends Animal{
	
}
