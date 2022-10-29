package test2;

// 구구단을 출력하시오.
// 2 x 1 = 2
// ...
// 9 x 1 = 9

// for(int i = 2; i < 10; i++) {
// System.out.println(i);
//for(int j = 1;j < 10;j++) {
// System.out.println(i + "," + j);
// }
// System.out.println();
//

public class test13 {

	public static void main(String[] args) {
for (int i = 2; i < 10; i++) {
	for(int j = 1; j < 10; j++) {
		System.out.println(i + " x " + j + " = " + (i * j));
	}
}
	}
}
