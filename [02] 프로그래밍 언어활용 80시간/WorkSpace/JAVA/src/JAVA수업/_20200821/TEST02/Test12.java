package JAVA수업._20200821.TEST02;

/*
 * Chapter 05
 * 실행 흐름의 컨트롤
 * Page : 119
 */
public class Test12 {
	public static void main(String[] args) {

		for (int i = 0; i <= 10; i++) {
			System.out.println(i);
		}
		
		int sum = 0;
		for (int j = 0; j <= 10; j++) {
			System.out.println(j);
			sum +=j;
		}
		System.out.println("sum = "+sum);
		
		for (int i = 0; i <= 10; i++) {
			for (int j = 0; j <= 10; j++) {
				System.out.print(" ["+i+"회전]\t[j:"+j+"수행] ");
			}
			System.out.println();
		}
		
	}//the end of main
}//the end of class
