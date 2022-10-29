package Chapter._18._1;

//394 PAGE
public class ExceptionMessage {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			md1(3);
		} catch (Throwable e) {
			e.printStackTrace();
		}
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

