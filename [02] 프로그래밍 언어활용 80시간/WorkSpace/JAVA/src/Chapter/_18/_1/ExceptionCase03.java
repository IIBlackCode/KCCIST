package Chapter._18._1;

import java.util.Scanner;

/*
 Exception in thread "main" java.util.InputMismatchException
	at java.util.Scanner.throwFor(Unknown Source)
	at java.util.Scanner.next(Unknown Source)
	at java.util.Scanner.nextInt(Unknown Source)
	at java.util.Scanner.nextInt(Unknown Source)
	at Chapter.Chapter18.ExceptionCase3.main(ExceptionCase3.java:13)
 */

//389 PAGE
public class ExceptionCase03 {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		@SuppressWarnings({ "unused", "resource" })
		Scanner scan = new Scanner(System.in);
		
		try {

			System.out.print("a/b ...a? ");
			int n1 = scan.nextInt();
			System.out.print("a/b ...b? ");
			int n2 = scan.nextInt();
			System.out.printf("%d /%d = %d \n", n1, n2, n1/n2);
			
		} catch (Exception e) {
			// TODO: handle exception
		}
		
		
		System.out.println("Good bye");
	}

}
