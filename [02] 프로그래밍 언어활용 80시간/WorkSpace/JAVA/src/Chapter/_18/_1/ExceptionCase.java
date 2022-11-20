package Chapter._18._1;

import java.util.Scanner;

// 384 PAGE
public class ExceptionCase {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		@SuppressWarnings({ "unused", "resource" })
		Scanner scan = new Scanner(System.in);
		
		System.out.print("a/b ...a? ");
		int n1 = scan.nextInt();
		System.out.print("a/b ...b? ");
		int n2 = scan.nextInt();
		
		
		System.out.printf("%d /%d = %d \n", n1, n2, n1/n2);
		System.out.println("Good bye");
	}

}
