package com.test3;

import com.test.calc.*;
import com.test2.test.MyClass;

public class Test1 {
	public static void main(String[] args) {
		Calculator c = new Calculator();
		int r = c.add(1, 2);
		System.out.println(r);
		MyClass.myMethod();
	}
}