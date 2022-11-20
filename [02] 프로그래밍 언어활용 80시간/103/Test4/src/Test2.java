class MyClass2 {
	public void message(String msg) {
		System.out.println(msg);
	}

	public String message2(String msg) {
		return msg;
	}
}

public class Test2 {
	public static void main(String[] args) {
	//	MyClass2 c;
	// c = new MyClass2();
		MyClass2 c2 = new MyClass2();
		c2.message("안녕하세요.");
		String s = c2.message2("반가워요.");
		System.out.println(s);
	}

}
