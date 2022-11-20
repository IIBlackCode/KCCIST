package test3;

public abstract class test9 {

	public static void message() { System.out.println("message");}
	public static void main(String[] args) {
		message();
		test9 t = new test9();
		t.message2();
	}
public void messsage2() {System.out.println("message2");}
}
