package test2;

public class test17 {
	public static void main(String[] args) {
//		for (int i = 1; i <= 9; i++) {
//			for (int j = 1; j <= 9; j++) {
////				System.out.print("*");
//				System.out.print("["+i+","+j+"] ");
//			}
//			System.out.println("");
//		}
//		System.out.println("===============================");
		
		for (int i = 1; i <= 9; i++) {
			for (int j = 1; j <= 9; j++) {
//				System.out.print("*");
				if (i+j <= 10) {
//					System.out.print("["+i+","+j+"] ");
					System.out.print("["+(i+j)+"] \t");
				}
				else {
					System.out.print(" ");
				}
			}
			System.out.println("");
		}
		
	}
}
