package JAVA수업._20200821.TEST02;
/*
 * Chapter 05
 * 실행 흐름의 컨트롤
 * Page : 119
 */
public class Test10 {
	public static void main(String[] args) {
		
		System.out.println("호출될 때 증가[초기값(0)에 +1된 상태에서 출력된다.]");
		int i = 1;
		int sum = 0;
		
		while(i<=10) {
			System.out.println(i);
			i++;	//호출될 때 증가
		}

		System.out.println("호출되고 증가[초기값(0)부터 호출된다]");
		int j = 0;
		while(j<=10) {
			System.out.println(j);
			++j; 	//호출되고 증가
		}
		
		System.out.println("호출될 때 증가되는 sum");
		int ii = 1;
		while(ii<=10) {
			sum += ii;
			System.out.println("[sum :"+sum+"]\t [i :"+ii+"]");
			ii++;	
		}
		System.out.println("[sum :"+sum+"]\t [i :"+ii+"]");
		
		
	}
}
