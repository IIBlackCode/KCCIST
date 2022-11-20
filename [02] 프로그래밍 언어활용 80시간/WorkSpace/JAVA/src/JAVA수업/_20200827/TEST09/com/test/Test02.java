package JAVA수업._20200827.TEST09.com.test;

class MyClass2 {
	
	/*
	 * Static 변수를 사용하는 이유
	 * 1. 변수를 공유해서 사용하고 싶을 때
	 * 2. Static 변수를 초기화 하고싶을 때 사용
	 */
	static int static_a;
	
	static {
		System.out.println("Static Block >> "+static_a);
	}
	
	public MyClass2() {
		// TODO Auto-generated constructor stub
		System.out.print("Default Contructor : ");
		static_a++;
		System.out.println("static_a = ["+static_a+"]");
	}
}

public class Test02 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		@SuppressWarnings("unused")
		MyClass2 c1 = new MyClass2();
		@SuppressWarnings("unused")
		MyClass2 c2 = new MyClass2();
	}

}
