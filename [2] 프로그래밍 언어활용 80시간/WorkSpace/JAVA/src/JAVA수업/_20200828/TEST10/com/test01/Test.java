package JAVA수업._20200828.TEST10.com.test01;

public class Test {
	public static void main(String[] args) {
		String str1 = "안녕하세요";
		String str2 = "안녕하세요";
		
		if (str1 == str2) {
			System.out.println("OK1");
		}
		String str3 = new String("안녕하세요");
		String str4 = new String("안녕하세요");
		if (str3 == str4) {
			System.out.println("OK2");
		}
		if (str3.equals(str4)) {
			System.out.println("OK3");
		}
	}
}
