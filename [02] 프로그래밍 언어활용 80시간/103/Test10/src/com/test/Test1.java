package com.test;
public class Test1 {
public static void main(String[] args) {
	String str1 = "æ»≥Á«œººø‰.";
	String str2 = "æ»≥Á«œººø‰.";
	if(str1 == str2) {System.out.println("O.K");}
	String str3 = new String("æ»≥Á«œººø‰.");
	String str4 = new String("æ»≥Á«œººø‰.");
	if(str3 == str4) {System.out.println("O.K2");}
	if(str3.equals(str4)) {System.out.println("O.K3");}
}
}
