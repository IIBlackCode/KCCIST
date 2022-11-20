package JAVA수업._20200916.TEST13.com.test01;

import java.util.ArrayList;
import java.util.List;

abstract class Shape {
	
	public Shape() {
		System.out.println("Shape 생성");
	}

	abstract void draw();
}

class Circle extends Shape{

	
	
	public Circle() {
		System.out.println("Create Circle Instance");
	}

	@Override
	void draw() {
		System.out.println("Circle draw");
	}
}

class Rectangle extends Shape{

	
	public Rectangle() {
		System.out.println("Rectangle draw");
	}

	@Override
	void draw() {
		System.out.println("Rectangle draw");
	}
}

public class Test01 {
	/*
	 * 제네릭 사용시 T만 사용하게 되면 for (T s : lists)에서 T가 명시적으로 정의되어있지 않아 에러 발생
	 * 이를 해결하고자 와일드카드(?:물음표) 사용
	 */
	static void drawShapes(List<? extends Shape> lists) {
		
		for (Shape s : lists) {
			s.draw();
		}
	}

	public static void main(String[] args) {
		
		/*ClassCastException Test*/
		Shape s = new Circle();
		
//		Circle c = (Circle)s;
//		Rectangle r = (Rectangle)s;
		
//		Circle c2 = new Circle();
//		Rectangle r2 = new Rectangle();
		
//		c2 = (Circle)r2;
//		r2 = (Rectangle)c2;
		
		ArrayList<Circle> list1 = new ArrayList<Circle>();
		list1.add(new Circle());
		list1.add(new Circle());
		
		ArrayList<Rectangle> list2 = new ArrayList<Rectangle>();
		list2.add(new Rectangle());
		list2.add(new Rectangle());
		
		
	}

}
