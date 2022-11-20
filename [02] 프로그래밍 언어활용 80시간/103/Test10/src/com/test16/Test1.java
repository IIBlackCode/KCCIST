package com.test16;

interface Printable {
	void print();
}
interface Showable extends Printable {
	void show();
}

class A3 implements Showable{
	public void print()  {System.out.println("print");}	
public void show() {System.out.println("show");}
}
public class Test1 {

	public static void main(String[] args) {

	}

}
