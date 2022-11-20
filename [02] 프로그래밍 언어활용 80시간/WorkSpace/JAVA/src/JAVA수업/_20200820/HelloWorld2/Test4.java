package JAVA수업._20200820.HelloWorld2;

public class Test4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a = 1;
		String b = "2";	
		String c = "3";	
		int d = 2;
		int e = a + d;
		
		System.out.println(e);
		System.out.println(b+c);
		
//		byteToBit(1);
//		byteToBit(2);
		byteToBit(4);
	}
	public static void byteToBit2(int byte2) {
	
	}
	
	public static void byteToBit(int byte2) {
		int bit2 = 0;
		bit2 = byte2 * 8;
//		System.out.println( byte2 + " BYTE : " + bit2 + " BIT");
		
		int i, j, cnt =0;
//		long res = 1;
		int res = 1;
		
		for (i = 0; i <= bit2; i++) {
			res = 1;
			for (j = 1; j <= i; j++) {
				res = 2 * res;
			}
			cnt++;
			System.out.println(cnt+"회전 ["+res+"]");
		}
		System.out.println(byte2+" BYTE("+bit2+" BIT"+")의 표현 가능 범위");
		System.out.println("2의" + (i-1) +"승 : "+ res);
		System.out.println(((res/2)*(-1))+" ~ "+((res/2)-1));
		
		System.out.println("=========================================");
		
		
	}
}
