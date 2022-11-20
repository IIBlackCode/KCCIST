package JAVA수업._20200915.TEST12.com.test02;

public class Test01 {
	static void add(int a, int b) {
		
	}
	static void add(String a, String b) {
		
	}
	
	//모든 타입을 받을 수 있음
	static void add2(Object a, Object b) {
		
	}
	
	//모든 타입을 받을 수 있음
	static void test1(Object b) {
		Integer i = (Integer)b;
	}
	//int형만 받을 수 있음
	static void test2(int b) {
		
	}
	
	
	public static void main(String[] args) {
		add2("test", "test2");
		add2(10, 10);
		Object o = 100;
		Integer o2 = 100;
		int o3 = o2;
		
		//Reference type
		String str = "이순신";	
		
		//Value type
		int a = 100;			
		
		//Object에서 Integer로 Casting하면 value type을 사용할 수 있음
		//즉, 값을 뽑아내기 위해 unboxing 필요
		Object oo1 = new Integer(100);
		
		//boxing
		Object oo2 = 100;
		int oo3 = (Integer)oo2;
		
		
	}
}
