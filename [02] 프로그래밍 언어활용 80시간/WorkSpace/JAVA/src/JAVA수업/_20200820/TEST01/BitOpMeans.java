package JAVA¼ö¾÷._20200820.TEST01;

public class BitOpMeans {

	public static void main(String[] args) {
		// 8 4 2 1
		byte n1 = 13; 				//1101
		byte n2 = 7;				//0111
		byte n3 = (byte) (n1 & n2);	//0101 = 5
		
		System.out.println(n3);
	}

}
