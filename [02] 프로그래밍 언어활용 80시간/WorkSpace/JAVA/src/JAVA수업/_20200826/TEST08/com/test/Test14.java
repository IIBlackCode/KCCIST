package JAVA수업._20200826.TEST08.com.test;

//객체 생성할때마다 Count
class MyClass{
	static int a = 10;
	
}

public class Test14 {
	public static void main(String[] args) {
		/*
		 *Static 변수는 instace 생성해서 접근이 가능하다.
		 *	1.static 접근
		 *	2.instance접근 둘다 가능
		 */
		System.out.println(MyClass.a);
		MyClass.a = 100;
		System.out.println(MyClass.a);

		MyClass b = new MyClass();
		System.out.println(b.a);
		b.a = 1000;
		System.out.println(MyClass.a);
	}
}
