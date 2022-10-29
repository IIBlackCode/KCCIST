package JAVA¼ö¾÷._20200828.TEST10.com.test11;

interface Calculate {
	int operate(int a, int b);
}
class Addition implements Calculate{

	@Override
	public int operate(int a, int b) {
		return a+b;
	}
	
}
class Subtraction implements Calculate{

	@Override
	public int operate(int a, int b) {
		return a-b;
	}
	
}
class Multiplication implements Calculate{

	@Override
	public int operate(int a, int b) {
		return a*b;
	}
	
}
class Division implements Calculate{

	@Override
	public int operate(int a, int b) {
		return a/b;
	}
	
}

class Calculator {
	Calculate c;
	Calculator(Calculate c) {
		this.c = c;
	}
	
	public int operate(int x, int y) {
		return c.operate(x, y);
	}
}


public class Test {
	public static void main(String[] args) {
		Calculator c = new Calculator(new Addition());
		System.out.println(c.operate(1, 2));
		Calculator c2 = new Calculator(new Subtraction());
		System.out.println(c.operate(4, 2));
		Calculator c3 = new Calculator(new Division());
		System.out.println(c.operate(4, 2));
		
	}
}
