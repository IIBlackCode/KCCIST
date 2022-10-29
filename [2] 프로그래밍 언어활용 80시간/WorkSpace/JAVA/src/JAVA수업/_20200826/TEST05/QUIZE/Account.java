package JAVA¼ö¾÷._20200826.TEST05.QUIZE;

public class Account {
	
	public static double interest;
	
	protected String accountNo;
	protected String accountName;
	protected int balance;

	protected Account(String accountNo, String accountName, int balance) {
		// TODO Auto-generated constructor stub
		this.accountNo = accountNo;
		this.accountName = accountName;
		this.balance = balance;
	}

	protected int deposit(int amount) {
		balance += amount;
		return balance;
		
	}

	protected void withdraw(int amount) {
		balance -= amount;
		return;
	}

	protected void addInterest() {
		// TODO Auto-generated method stub
		balance = balance+(int)(balance*interest);
		
	}

	protected static double getInterest() {
		return interest;
	}

	protected static void setInterest(double interest) {
		Account.interest = interest;
	}

	protected String getAccountNo() {
		return accountNo;
	}

	protected void setAccountNo(String accountNo) {
		this.accountNo = accountNo;
	}

	protected String getAccountName() {
		return accountName;
	}

	protected void setAccountName(String accountName) {
		this.accountName = accountName;
	}

	protected int getBalance() {
		return balance;
	}

	protected void setBalance(int balance) {
		this.balance = balance;
	}

}
