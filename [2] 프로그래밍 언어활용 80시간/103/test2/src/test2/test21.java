package test2;

public class test21 {

	public static void main(String[] args) {
		for (int i = 1; i <= 10; i++) {
			// if (i == 5) {
			// continue;
			// }
			System.out.println(i);
		}
		System.out.println();
		int j = 1;
		while (j <= 10) {
			if (j == 5) {
				j++;
				continue;
			}
			System.out.println(j);
			j++;
		}
	}

}
