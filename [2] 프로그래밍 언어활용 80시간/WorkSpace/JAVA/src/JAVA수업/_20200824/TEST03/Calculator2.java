package JAVA수업._20200824.TEST03;
public class Calculator2 {
	public int pluse(int value1, int value2) {
		int result = value1 + value2;
		System.out.println(value1 + " + " + value2 + " = " + result);
		return result;
	}

	public int minus(int value1, int value2) {
		int result = value1 - value2;
		System.out.println(value1 + " - " + value2 + " = " + result);
		return result;
	}

	public int multiply(int value1, int value2) {
		int result = value1 * value2;
		System.out.println(value1 + " X " + value2 + " = " + result);
		return result;
	}

	public int divide(int value1, int value2) {
		int result = value1 / value2;
		System.out.println(value1 + " / " + value2 + " = " + result);
		System.out.println("몫 : "+result);
		System.out.println("나머지 : "+value1%value2);
		return result;
	}
}//The end of class