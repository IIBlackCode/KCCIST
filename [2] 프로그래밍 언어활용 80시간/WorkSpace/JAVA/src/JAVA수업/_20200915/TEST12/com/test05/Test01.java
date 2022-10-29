package JAVA¼ö¾÷._20200915.TEST12.com.test05;

class Orange {
	
}

class Box<T> {
	
	private T o;

	public Box() {
	}
	public Box(T o) {
		super();
		this.o = o;
	}
	public T getO() {
		return o;
	}

	public void setO(T o) {
		this.o = o;
	}
}//The end of Box class

public class Test01 {
	public static void main(String[] args) {
		Box<String> b = new Box<String>();
		b.setO("È«±æµ¿");
		System.out.println(b.getO());
		Box<String> b2 = new Box<String>();
	}
}
