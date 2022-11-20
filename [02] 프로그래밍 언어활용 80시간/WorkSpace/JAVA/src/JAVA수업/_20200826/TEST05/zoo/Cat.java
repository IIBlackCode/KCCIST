package JAVA수업._20200826.TEST05.zoo;

public class Cat {
	
	//다른 패키지에서 접근할 수 있도록 public 선언
	public void makeSound() {
		System.out.println("makeSound");
	}
	
	//zoo패키지에서만 접근할 수 있다.
	void makeHappy() {
		System.out.println("makeHappy");
	}
}
