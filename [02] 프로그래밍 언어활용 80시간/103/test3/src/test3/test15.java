package test3;

public class test15 {

	public static void main(String[] args) {
BankAccount acc = new BankAccount();
System.out.println(acc.checkBalance());
acc.deposit(10000);
acc.checkBalance();
acc.withdraw(5000);
acc.checkBalance();
	}

}
