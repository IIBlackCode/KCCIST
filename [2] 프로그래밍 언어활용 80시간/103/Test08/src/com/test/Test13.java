package com.test;

class Counter {
	static int count = 0;
int count2 = 0;
	Counter() {
		count++;
		System.out.println(count);
	}
	static int getCount() {
		return count;
	}
int getCount2() {
	return count;
}
}

public class Test13 {

	public static void main(String[] args) {
		Counter c = new Counter();
		Counter c2 = new Counter();
		Counter c3 = new Counter();
		
		System.out.println(Counter.getCount());
	}
}