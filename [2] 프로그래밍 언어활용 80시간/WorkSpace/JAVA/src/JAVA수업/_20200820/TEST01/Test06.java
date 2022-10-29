package JAVA수업._20200820.TEST01;

import javax.swing.border.EmptyBorder;

public class Test06 {
	public static void main(String[] args) {
	
		short shortt = Short.MAX_VALUE;
		System.out.println(shortt);
		long longg = Long.MAX_VALUE;
		System.out.println(longg);
		long longg2 = shortt;
		System.out.println(longg2);
		short shortt2 = (short) longg2;
		System.out.println(shortt2);
		
		float float1 = 0.23f;
		double double1 = 0.23f;
//		float float3 = 0.23d;// 형변환 필요
	}
}
