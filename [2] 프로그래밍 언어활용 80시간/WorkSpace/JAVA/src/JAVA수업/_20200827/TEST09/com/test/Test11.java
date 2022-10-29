package JAVA수업._20200827.TEST09.com.test;

class MyClass3 { // Default로 Object를 상속받는다.
	int a;
}

class MyClass4 { // Default로 Object를 상속받는다.
	
}

public class Test11 {
	public static void main(String[] args) {
		
		MyClass3 test = new MyClass3();
		test.a = 10;
		Object o = new MyClass3();
		
		Object oo = test;
		
		MyClass3 mc3 = (MyClass3) oo;
		int aa = mc3.a;
		System.out.println(aa);
	}
}
