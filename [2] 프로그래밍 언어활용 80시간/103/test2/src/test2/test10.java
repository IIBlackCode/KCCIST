package test2;

public class test10 {

	public static void main(String[] args) {
		int i = 1;
		int sum = 0;
		while (i <= 10) {
//			System.out.println(i);
//			1 = 0 + 1 
//			3 = 1 + 2 
//			6 = 3 + 3
//			sum = sum + i;
			sum += i;
//			System.out.println(sum + "," + i);
			i++;
		}
System.out.println(sum);

	}

}
