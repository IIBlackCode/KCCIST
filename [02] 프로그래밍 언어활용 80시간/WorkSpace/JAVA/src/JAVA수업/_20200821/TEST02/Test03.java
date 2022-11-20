package JAVA수업._20200821.TEST02;

/*
 * Chapter 05
 * 실행 흐름의 컨트롤
 * 104Page
 */
public class Test03 {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
//		int age = 20;
		int age = 16;
		int grade = 1;
		
		/*True*/
		if(age > 17) {	// (괄호 내용의 값) > True False 
			System.out.println("True : 17살보다 크다\n 공부하다");
		}else {
			System.out.println("False : 17보다 작습니다.");
		}
		
		/*False*/
		if(age < 17) {	// (괄호 내용의 값) > True False 
			System.out.println("참인 경우 : 17살보다 크다");
		}
		
		/* 
		 * == 	: 비교연산자
		 * =	: 대입연산자
		 */
		if (grade  == 1) {
			System.out.println("당신의 등급은 1입니다.");
		}
		
		/*
		 * 조건문이 한줄일 때 괄호생략이 가능하다
		 */
		
		if (grade  == 1) 
			System.out.println("당신의 등급은 1입니다.");
		
	}

}
