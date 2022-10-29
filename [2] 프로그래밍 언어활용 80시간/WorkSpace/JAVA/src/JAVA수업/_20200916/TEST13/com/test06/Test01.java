package JAVA수업._20200916.TEST13.com.test06;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;


public class Test01 {

	public static void main(String[] args) {
		
		ArrayList<String> al = new ArrayList<String>();
		al.add("10");
		al.add("20");
		List<String> al2 = new ArrayList<String>();
		al2.add("10");
		al2.add("20");
		
		/*
		 Iterator를 사용하여 리스트 출력하기
		 */
		Iterator<String> s = al.iterator();
		while (s.hasNext()) {
			String str = s.next();
			System.out.println(str);
		}
		
		for (Iterator<String> s2 = al2.iterator();	s.hasNext();) {
			String str = s2.next();
			System.out.println(str);
		}
	}

}
