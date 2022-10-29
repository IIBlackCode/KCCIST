package JAVA수업._20200915.TEST12.com.test03;

import java.util.ArrayList;

public class Test01 {
	public static void main(String[] args) {
		ArrayList al = new ArrayList();
		
		/*
		 * ArrayList 는 Object타입으로 받기 때문에 다양한 값을 받을 수 있다.
		 */
		
		al.add(100);
		al.add("홍길동");
		al.add(19.20);
		
		Object o = al.get(0);
		System.out.println(((Integer)o).intValue());
		
		Object o2 = al.get(1);
		String s = (String)o2;
		System.out.println(s);
		
	}
}
