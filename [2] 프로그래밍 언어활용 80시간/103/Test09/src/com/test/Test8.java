package com.test;
class Animal2 {
	void breath() {System.out.print("Animal2 breath"); }
}
class Dog2 extends Animal2 {
	void bark() {System.out.println("Dog2 bark"); }
	
}
public class Test8 {
	public static void main(String[] args) {
		
		Dog2 d = new Dog2();
		Animal2 a = d;
		a.breath();
		
//	int a = 100;
//	long b = a; // implicit cast (conversion)
//	long c = Long.MAX_VALUE;
//	int d = (int)c; //explicit cast(conversion)
	}

}

