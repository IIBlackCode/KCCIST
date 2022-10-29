package JAVA수업._20200826.TEST05.animal;

import JAVA수업._20200826.TEST05.zoo.Cat;

public class Dog {
	
	static void welcom(JAVA수업._20200826.TEST05.zoo.Cat o2) {
		o2.makeSound();
//		o2.makeHappy();
	}
	public static void main(String[] args) {
		
		Cat o = new Cat();
		welcom(o);
		
	}
	public void welcom0(JAVA수업._20200826.TEST05.zoo.Cat c) {
		c.makeSound();
//		c.makeHappy();
	}
}
