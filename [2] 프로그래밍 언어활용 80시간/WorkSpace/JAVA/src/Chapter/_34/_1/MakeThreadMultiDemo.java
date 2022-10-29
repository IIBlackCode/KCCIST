package Chapter._34._1;import java.util.FormatFlagsConversionMismatchException;

public class MakeThreadMultiDemo {
	public static void main(String[] args) {
		//20미만 짝수 출력
		Runnable task1 = () -> {
			
			try {
				for (int i = 0; i < 2000; i++) {
					if (i%2 == 0) {
						System.out.println(i + " Ddos attack!! ");
					}
				}
			} catch (FormatFlagsConversionMismatchException e) {
				// TODO: handle exception
				e.printStackTrace();
			}
			
		};
		//20미만 홀수 출력
		Runnable task2 = () -> {
			
			try {
				for (int i = 0; i < 200; i++) {
					if (i%2 != 0) {
						System.out.println(i + " Ddos attack!! ");
					}
				}
			} catch (FormatFlagsConversionMismatchException e) {
				// TODO: handle exception
				e.printStackTrace();
			}
			
		};
		
		Thread t1 = new Thread(task1);
		Thread t2 = new Thread(task2);
		t1.start();
		t2.start();
	}
	
}
