package JAVA수업._20200916.TEST13.com.test03;

import java.util.ArrayList;
import java.util.List;

class A {}
class B extends A {}
class C extends A {}

public class Test01 {
	/*
	 * 						<? extends Number> 	바인딩 : 제약이 걸린 상태, extends가 걸려있음
	 * 						<?> 				바인딩 : 제약이 없는 상태, extends가 없음
	 */
	static void testList(List<? extends Number> list) {
		for (Object a : list ) {
			System.out.println(a.toString());
		}
	}//The end of method
	
	public static void main(String[] args) {
		List<A> list1 = new ArrayList<A>();
		List<B> list2 = new ArrayList<B>();
	}//The end of main Method
	
}//The end of Main class
