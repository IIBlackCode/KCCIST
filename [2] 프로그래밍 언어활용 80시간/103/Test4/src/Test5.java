class MyClass5 {
	public int a;
}

public class Test5 {
	public static void test2(MyClass5 b) { //MyClass5 b = c
		b.a++;
		System.out.println(b.a); //101
	}
public static void main(String[] args) {
	MyClass5 c = new MyClass5();
	c.a = 100;
	System.out.println(c.a);
	test2(c);
	System.out.println(c.a); //101

		int a = 10;
		test(a);
		System.out.println(a);
	}

	public static void test(int b) {
		b++;
		System.out.println(b);
	}
}