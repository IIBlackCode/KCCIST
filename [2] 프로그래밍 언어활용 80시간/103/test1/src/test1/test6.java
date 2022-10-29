package test1;

public class test6 {
public static void main(String[] args) {
	short s = Short.MAX_VALUE;
	System.out.println(s);
	long l = Long.MAX_VALUE;
	System.out.println(l);
	long l2 = s;
	System.out.println(l2);
	short s2 = (short)l2;
	System.out.println(s2);
	
	float f2 = 0.23f;
	double d2 = 0.23d;
//	float f3 = 0.23d;
}
}