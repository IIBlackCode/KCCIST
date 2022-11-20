package com.test14;
interface Printable {
	void print();
}

interface Showable {
	void show();
}

class A5 implements Printable, Showable {
	public void show() {System.out.println("show");}
	public void print() {System.out.println("print");}
}

public class Test1 {

	public static void main(String[] args) {
A5 a = new A5();
a.print(); a.show();

	}

}
