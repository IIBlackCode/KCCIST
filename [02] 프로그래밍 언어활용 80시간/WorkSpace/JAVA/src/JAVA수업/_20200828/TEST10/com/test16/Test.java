package JAVA¼ö¾÷._20200828.TEST10.com.test16;

interface Printable {
	void print();
}
interface Showable extends Printable{
	void show();
}

class A3 implements Showable {

	@Override
	public void print() {
		// TODO Auto-generated method stub
		System.out.println("print");
	}

	@Override
	public void show() {
		// TODO Auto-generated method stub
		System.out.println("show");
	}
	
}

public class Test {
	public static void main(String[] args) {
		
	}
}
