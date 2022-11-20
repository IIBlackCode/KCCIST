package JAVA수업._20200825.TEST04.com.test.run;

import JAVA수업._20200825.TEST04.com.mycompany.module.MyClass2;

public class Test01 {
	public static void main(String[] args) {
		MyClass c = new MyClass();//같은 패키지경로에 있을시 import가 필요없다.
		c.aMethod();
		
		//패키지 경로가 다를 경우 import를 사용한다.
		MyClass2 c2 = new MyClass2();
		c2.aMethod();
	}
}
