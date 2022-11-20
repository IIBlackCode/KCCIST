package Chapter._18._1;

//395 PAGE
public class ExceptionMessage2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		md1(3);
		System.out.println("Good bye!");
	}
	
	public static void md1(int n) {
		md2(n,0);
	}

	public static void md2(int n1, int n2) {
		@SuppressWarnings("unused")
		int r = n1 / n2;
	}
	
}

