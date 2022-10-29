package JAVA수업._20200820.HelloWorld2;

public class Test3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(7);
		System.out.println(3.15);

		// 문자열 + 정수형 = 정수형 
		System.out.println("3 + 5 = " + 8);
		System.out.println(3.15 + "는 실수입니다.");
		System.out.println("3 + 5" +" 의 연산 결과는 8입니다."+ 8);
		System.out.println(3 + 5);
		
		math(3, 5);
	
	}
	
	public static void math(int a, int b) {
		System.out.println(a + " + " + b + " = "+ (a+b));
		System.out.println(a + " - " + b + " = "+ (a-b));
		System.out.println(a + " * " + b + " = "+ (a*b));
		System.out.println(a + " / " + b + " = "+ (a/b));
	}

}
