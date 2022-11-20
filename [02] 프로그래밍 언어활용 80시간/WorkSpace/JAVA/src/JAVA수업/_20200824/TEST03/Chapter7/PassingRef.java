package JAVA¼ö¾÷._20200824.TEST03.Chapter7;

public class PassingRef {
	public static void main(String[] args) {
		BankAccount ref = new BankAccount("ref");
		
		ref.deposit(3000);
		ref.withdraw(300);
		check(ref);
		
	}
	
	public static void check(BankAccount acc) {
		acc.checkMyBalance();
	}
}
