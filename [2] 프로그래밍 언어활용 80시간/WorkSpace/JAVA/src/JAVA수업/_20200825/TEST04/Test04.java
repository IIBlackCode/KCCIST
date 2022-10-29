package JAVA수업._20200825.TEST04;

import JAVA수업._20200820.HelloWorld2.Test;

public class Test04 {
	public static void main(String[] args) {
		MyClass4 myClass1 = new MyClass4();
		System.out.println("초기화가 되지 않은 변수 출력"
				+ "\nmyClass1.a : "+myClass1.a);
		System.out.println("myClass1.b : "+myClass1.b);
		
		//setter
		myClass1.a = 10;
		
		//getter
		System.out.println("myClass1.a :"+myClass1.a);
		
		myClass1.b = "이순신";
		System.out.println("myClass1.b :"+myClass1.b);
	
		
		MyClass4 myClass2 = myClass1;
		System.out.println("****  myClass2 = myClass1  ****");
		
		System.out.println("myClass2 : "+myClass2.a +", "+myClass2.b);
		
		System.out.println("myClass2.a = 30, myClass2.b = \"세종대왕\" ");
		myClass2.a = 30;
		myClass2.b = "세종대왕";
		
		System.out.println(myClass2.a);
		System.out.println(myClass1.b);
		
		int x = 100;
		test(x);
		System.out.println("int x : "+x);
	}
	
	static void test(int x) {
		x = 20;
		System.out.println("test() : "+x);
	}
}

class MyClass4{
	public int a;
	public String b;
}