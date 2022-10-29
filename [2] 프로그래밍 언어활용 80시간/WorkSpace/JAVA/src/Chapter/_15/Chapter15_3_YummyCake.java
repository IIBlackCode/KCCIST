package Chapter._15;

class Cake{
	
}
class CheeseCake extends Cake {
	
}
class StrawberryCake extends CheeseCake {
	
}

public class Chapter15_3_YummyCake {
	public static void main(String[] args) {
		
//		Cake cake = new Cake();
//		Cake cake = new CheeseCake();
		Cake cake = new StrawberryCake();
				
		if (cake instanceof Cake) {
			System.out.println("1. Cake instance or inherit Cake \n");
		}else {
			System.out.println("1. false");
		}
		
		if (cake instanceof CheeseCake) {
			System.out.println("2. Cake instance or inherit Cake \n");
		}else {
			System.out.println("2. false");
		}
		if (cake instanceof StrawberryCake) {
			System.out.println("3. Cake instance or inherit Cake \n");
		}else {
			System.out.println("3. false");
		}
			
	}
}
