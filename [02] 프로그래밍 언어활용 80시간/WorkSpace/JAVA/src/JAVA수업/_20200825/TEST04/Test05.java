package JAVA수업._20200825.TEST04;

import JAVA수업._20200820.HelloWorld2.Test;

public class Test05 {
	public static void main(String[] args) {
		
		MyClass5 c = new MyClass5();
		c.a = 100;
		System.out.println(c.a);
		test2(c);
		System.out.println(c.a);
		
	}
	
	static void test2(MyClass5 b) {
		b.a++;
		System.out.println(b.a);
	}
}

class MyClass5{
	public int a;
}