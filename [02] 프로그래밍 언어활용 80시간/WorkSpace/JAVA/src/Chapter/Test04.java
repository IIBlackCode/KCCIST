package Chapter;

import java.util.Scanner;

import JAVA수업._20200824.TEST03.Calculator;
import JAVA수업._20200824.TEST03.Calculator2;

//클래스 생성시 public이 들어가는 클래스는 독립적인 파일을 생성해야한다.
public class Test04 {
	@SuppressWarnings("static-access")
	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner scan = new Scanner(System.in);
		
		System.out.print("value1 값을 입력 하시오 :");
		int value1 = scan.nextInt();
		System.out.print("value2 값을 입력 하시오 :");
		int value2 = scan.nextInt();
		
		//Static Method는 인스턴스를 생성하지 않아도 사용이 가능하다.
		Calculator calculator = new Calculator();
		calculator.pluse(value1, value2);
		Calculator.minus(value1, value2);
		calculator.multiply(value1, value2);
		Calculator.divide(value1, value2);
		
		//인스턴스 Method는 인스턴스를 생성해야 사용할 수 있다.
		Calculator2 calculator2 = new Calculator2();
		calculator2.pluse(value1, value2);
		calculator2.minus(value1, value2);
		calculator2.multiply(value1, value2);
		calculator2.divide(value1, value2);
		
		/**
		 * 인스턴스란?
		 * Stack heap
		 */
		
	}
	
}//end of class