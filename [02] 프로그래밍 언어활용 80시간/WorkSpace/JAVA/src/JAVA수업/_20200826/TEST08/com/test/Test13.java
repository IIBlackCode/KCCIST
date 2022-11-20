package JAVA수업._20200826.TEST08.com.test;

//객체 생성할때마다 Count
class Counter {
	int instanceCount = 0;
	static int staticCount = 0;
	
	public Counter() {
		instanceCount ++;
		staticCount++;
		System.out.println("count:"+instanceCount+", staticCount:"+staticCount);
	}

	public int getInstanceCount() {
		return instanceCount;
	}

	public void setInstanceCount(int instanceCount) {
		this.instanceCount = instanceCount;
	}

	public static int getStaticCount() {
		return staticCount;
	}

	public static void setStaticCount(int staticCount) {
		Counter.staticCount = staticCount;
	}
}

public class Test13 {
	public static void main(String[] args) {
		Counter c = new Counter();
		Counter c2 = new Counter();
		Counter c3 = new Counter();
		
		System.out.println(Counter.getStaticCount());
	}
}
