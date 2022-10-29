package com.test;

public class Test6 {

	static void test(int[] b) {
		for (int j = 0; j < b.length; j++) {
			System.out.println(b[j]);
		}
	}

	public static void main(String[] args) {
		int[] a = new int[2];
		a[0] = 100;
		a[1] = 200;
		test(a); // int[] b = a
	}

}
