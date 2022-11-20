package JAVA¼ö¾÷._20200820.TEST01;

import javax.swing.border.EmptyBorder;

public class Test07 {
	public static void main(String[] args) {
		int a = 10;
		int b = 10;
		System.out.println(a++ + ++a); //10 + 12 = 22
		System.out.println(b++ + b++); //10 + 11 = 22
		
		for (int i = 0; i <= 10; i++) {
			System.out.println(i);
		}// The end of for
		
		int y = 0;
		while (y <= 10) {
			System.out.println(y);
			y++;
		}//The end of while
	}// The end of Main method
}//The end of class
