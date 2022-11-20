package JAVA수업._20200827.TEST09.com.test;

public class Test04 {
	public static void main(String[] args) {
		int a = 0;
		int b = 0;
		String ln = "\n";
		String line = "==========================================";
		System.out.println(ln.concat(line));
		String test = "ABCDEFGH";
		String subString = test.substring(2);
		System.out.println("test : "+test);
		System.out.println("test.substring(2) : "+subString);
		System.out.println("test.charAt(1) : "+test.charAt(1));
		System.out.println("test.charAt(2) : "+test.charAt(2));
		System.out.println("test.charAt(3) : "+test.charAt(3));
		System.out.println("test.charAt(4) : "+test.charAt(4));
		System.out.println("test.charAt(5) : "+test.charAt(5));
		System.out.println("test.charAt(6) : "+test.charAt(6));
		System.out.println("test.charAt(7) : "+test.charAt(7));
		for (int i = 0; i < 10; i++) {
		try {
				System.out.println("test.charAt("+i+") : "+test.charAt(i));
		} catch (StringIndexOutOfBoundsException e) {
			System.out.println("test.charAt("+i+")번 인덱스에서 예외 발생 : "+e.getStackTrace());
			System.out.println("getStackTrace() : "+e.getMessage());
			}
		}
		subString = test.substring(2,5);
		System.out.println("test.substring(2,5) : "+subString);
		System.out.println("==========================================\n\tint a=0; \n\tint b = 0;\n");
		System.out.println("\tif (a == b)");
		if (a == b) {
			System.out.println("\tOK\n==========================================");
		}
		
		String s = new String("A");	//새로운 객체 생성 > 새로운 주소값 할당
		String s2 = new String("A");//새로운 객체 생성 > 새로운 주소값 할당
		System.out.println("\tString s = new String(\"A\");\n\tString s2 = new String(\"A\");\n");
		System.out.println("\tif (s == s2) {");
		if (s == s2) {
			System.out.println("\t같은 주소값을 바라보고 있다.\n==========================================");
		}else {
			System.out.println("\t서로 다른 주소값을 바라보고 있다.\n==========================================");
		}
		
		System.out.println("\tif (s.equals(s2))\n");
		if (s.equals(s2)) {
			System.out.println("\t문자열이 같다.\n==========================================");
		}else {
			System.out.println("\t문자열이 서로 다르다\n==========================================");
		}
		
		String s3 = s;
		System.out.println("\tString s3 = s;\n");
		System.out.println("\tif (s == s3)");
		if (s == s3) {
			System.out.println("\t같은 주소값을 바라보고 있다.\n==========================================");
		}else {
			System.out.println("\t서로 다른 주소값을 바라보고 있다.\n==========================================");
		}
		
		String s4 = "A";
		String s5 = "A";
		System.out.println("\tString s4 = \"A\";\n\tString s5 = \"A\";\n");
		System.out.println("\tif (s4 == s5)");
		if (s4 == s5) {
			System.out.println("\t같은 주소값을 바라보고 있다.\n==========================================");
		}else {
			System.out.println("\t서로 다른 주소값을 바라보고 있다.\n==========================================");
		}
	}
}
