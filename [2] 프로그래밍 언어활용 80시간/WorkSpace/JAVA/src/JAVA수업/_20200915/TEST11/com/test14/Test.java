package JAVA수업._20200915.TEST11.com.test14;

/*
 * 20-1	래퍼 클래스
 * PAGE : 442
 */

public class Test {
	public static void main(String[] args) {
		
		int a= 1;
		//Boxing : 값을 인스턴스에 감싸는 행위
		//인스턴스의 생성을 통해 이루어진다.
		Integer a2 = new Integer(10);	
		
		System.out.println(a+" + "+a2 + " = " + (a + a2));
		
		//Unboxing : 저장된 값을 꺼내는 행위
		//래퍼클래스에 정의된 메소드의 호출을 통해 이루어진다.
		int a3 = a2.intValue(); 
		
		//Auto Boxing
		Integer a4 = 12; 
		
		Integer a5 = new Integer(20);

		//Auto Unboxing
		int a6 = a5;
		
		Integer b1 = new Integer(10);
		Integer b2 = new Integer(20);
		Integer c1 =  b1 + b2;
		System.out.println(c1);
		
		
	}//The end of main Method
}//The end of class
