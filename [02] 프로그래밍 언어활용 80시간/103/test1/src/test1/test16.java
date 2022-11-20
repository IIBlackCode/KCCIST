package test1;

public class test16 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
int num1 = 0;
int num2 = 0;
boolean result;

result = ((num1 += 10) < 0) && ((num2 += 10) > 0);
System.out.println("result = " + result);
System.out.println("num1 = " + num1);
System.out.println("num2 = " + num2 + '\n');  // '\n'Àº °³ Çà

result = ((num1 += 10) > 0) || ((num2 += 10) > 0);
System.out.println("result = " + result);
System.out.println("num1 = " + num1);
System.out.println("num2 = " + num2);

//89p
	}

}
