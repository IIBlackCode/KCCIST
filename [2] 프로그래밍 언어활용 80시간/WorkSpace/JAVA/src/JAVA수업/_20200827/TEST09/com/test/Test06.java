package JAVA수업._20200827.TEST09.com.test;

class Animal {
	void eat() {
		System.out.println("eating...");
	}
	@SuppressWarnings("unused")
	private void privateMethod() {
		System.out.println("접근제어자가 private 이면 상속이 되더라도 접근이 되지 않는다.");
	}
}

class Dog extends Animal {
	void bark() {
		System.out.println("barking...");
	}
}

class BabyDog extends Dog {
	void weep() {
		System.out.println("weeping...");
	}
}
/*
 *	재사용 목적
 *	하위의 클래스에서 상속을 받아 기존의 코드를 재사용
 */
public class Test06 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		BabyDog bd = new BabyDog();
		bd.eat();
		bd.bark();
		bd.weep();
//		bd.privateMethod(); //private는 접근 불가
		
	}

}
