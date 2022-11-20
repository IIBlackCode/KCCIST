package JAVA¼ö¾÷._20200828.TEST10.com.test17;
/*
 * Default Method
 */
interface Drawable {
	void draw();
	default void msg() {
		System.out.println("msg");
	}
	static void draw2() {
		System.out.println("draw2");
	}
}

class Rectangle implements Drawable {

	@Override
	public void draw() {
		System.out.println("Rectangle");
	}
	
}

public class Test {
	public static void main(String[] args) {
		Drawable d = new Rectangle();
		d.draw();
		Drawable.draw2();
	}
}
