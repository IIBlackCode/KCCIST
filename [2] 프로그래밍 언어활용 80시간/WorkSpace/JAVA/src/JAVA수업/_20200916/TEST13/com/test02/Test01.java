package JAVA¼ö¾÷._20200916.TEST13.com.test02;

import java.util.ArrayList;
import java.util.List;

public class Test01 {
	
	static <T> void test(List<T> list) {	}
	static void test2(List<?> list) {	}
	
	/*
	 * 
	 */
	static Double add(ArrayList<? extends Number> num ) {
		double sum = 0;
		for (Number n : num) {
			sum = sum + n.doubleValue();
		}
		return sum;
		
	}
	
	public static void main(String[] args) {
		
		ArrayList<Integer> al = new ArrayList<Integer>();
		al.add(10);
		al.add(20);
		
		System.out.println(add(al));
	}
}
