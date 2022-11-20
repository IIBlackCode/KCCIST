package JAVA¼ö¾÷._20200828.TEST10.com.test14;

interface Printable {
	void print();
}
interface Showable {
	void show();
}
class A5 implements Printable, Showable {

	@Override
	public void show() {
		// TODO Auto-generated method stub
		System.out.println("show");
	}

	@Override
	public void print() {
		// TODO Auto-generated method stub
		System.out.println("print");
	}
	
}

public class Test {
	public static void main(String[] args) {
		A5 a = new A5();
		a.print();
		a.show();
	}
}
