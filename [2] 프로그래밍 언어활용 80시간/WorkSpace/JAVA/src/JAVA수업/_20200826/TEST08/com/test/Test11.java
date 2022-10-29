package JAVA¼ö¾÷._20200826.TEST08.com.test;

public class Test11 {
	public static void main(String[] args) {
		int[][] c = new int[3][];
		c[0] = new int[1];
		c[1] = new int[2];
		c[2] = new int[3];
		
		
		c[0][0] = 100;
		c[1][0] = 100;
		c[1][1] = 100;
		
		System.out.println(c[0][0]);
		System.out.println(c.length);
		System.out.println(c[0].length+", "+c[1].length+", "+c[2].length);
		for (int i = 0; i < c.length; i++) {
			for (int j = 0; j < c[i].length; j++) {
				System.out.println(c[i][j]);
			}
		}
		
	}
}
