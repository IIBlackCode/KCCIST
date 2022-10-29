package JAVA¼ö¾÷._20200916.TEST13.com.test12;

interface Calc {
	int add(int a, int b);
}

public class Test01 {

	public static void main(String[] args) {
		
		Calc c = (x,y) ->{return x + y;};
		int d = c.add(9, 20);
		System.out.println(d);
	}

}
