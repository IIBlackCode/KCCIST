package JAVA수업._20200828.TEST10.com.test19;

interface Database {
	void open();
//	void close();
}

abstract class RDBMS implements Database{
	static {
		System.out.println("TEST");
	}
	public RDBMS() {
		/*
		 * 인스턴스가 생성되지 않아도 생성자는 호출된다.
		 */
		System.out.println("Default RDBMS Constructor");
		
	}
	//Override가 나타나지 않음
//	public abstract void open();
	public void open() {
		System.out.println("RDBMS");
	}
	//추상클래스를 선언하면 해당 클래스를 상속받는 클래스에서 Override로 구현해야한다.
	public abstract void close(); 
}

class Oracle extends RDBMS {

	//무조건 Override
	@Override
	public void open() {
		System.out.println("Oracle");
	}

	@Override
	public void close() {
		// TODO Auto-generated method stub
		
	}
	
}

public class Test {
	public static void main(String[] args) {
		Oracle o = new Oracle();
		o.open();
		Database d = new Oracle();
		d.open();
	}
}
