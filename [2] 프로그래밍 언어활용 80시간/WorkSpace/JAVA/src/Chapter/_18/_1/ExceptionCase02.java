package Chapter._18._1;

import java.util.Scanner;

//387 PAGE
public class ExceptionCase02 {

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
			System.out.println("예외 발생 : "+e.getMessage());
		}
		
		
		
		System.out.println("Good bye");
	}

}
