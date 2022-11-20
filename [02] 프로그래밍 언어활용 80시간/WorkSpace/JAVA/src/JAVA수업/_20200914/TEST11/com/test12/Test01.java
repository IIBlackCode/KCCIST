package JAVA수업._20200914.TEST11.com.test12;

import java.util.Scanner;

class CheckAge extends Exception {
	public CheckAge(String message) {
		super(message);
	}
}

public class Test01 {
	
	static void checkAge(int age) throws CheckAge{
		if (age <= 18) {
			throw new CheckAge("당신은 18세 이하입니다.");
		} else {
			System.out.println("당신은 19세 이상입니다.");
		}
	}
	
	public static void main(String[] args) {
		
		
		System.out.println("당신의 나이를 입력해 주세요");
		Scanner kb = new Scanner(System.in);
		int age = kb.nextInt();
		
		try {
			checkAge(age);
		} catch (CheckAge e) {
			System.out.println(e.getMessage());
		} catch (Exception e) {
			// TODO: handle exception
			System.out.println("Exception : "+e.getMessage());
		} finally {
			System.out.println("종료");
		}
		
		
	}

}
