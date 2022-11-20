package JAVA수업._20200916.TEST13.com.test09;

/*
 * 매개변수의 가변인자 선언
 */

public class Test01 {
	
	
	static void display(String...vars) {
		for(String s : vars) {
			System.out.print(s+" ");
		}
		System.out.println();
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		display("홍길동");
		display("홍길동","이순신");
		display("홍길동","이순신","장영실");
	}

}
