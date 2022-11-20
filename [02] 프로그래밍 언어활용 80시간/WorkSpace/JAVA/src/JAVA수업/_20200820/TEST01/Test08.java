package JAVA¼ö¾÷._20200820.TEST01;

public class Test08 {

	public static void main(String[] args) {
		int a = 10;
		int b = 10;
		System.out.println(a++ + ++a); // 10 + 12 = 22
		System.out.println(b++ + b++); // 10 + 11 = 21
		
		for(int x = 0; x <= 10; x ++) {
			System.out.println(x);
		}
		
		int y = 0;
		while(y <= 10) {
			System.out.println(y);
			y++;
		}

	}

}
