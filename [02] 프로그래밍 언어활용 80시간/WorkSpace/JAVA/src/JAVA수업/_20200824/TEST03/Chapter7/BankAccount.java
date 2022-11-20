package JAVA수업._20200824.TEST03.Chapter7;
public class BankAccount {
	
	public String name = "";
	public int balance = 0;

	public BankAccount() {
		super();
	}

	public BankAccount(String name) {
		super();
		this.name = name;
	}
	
	//입금
	public int deposit(int amount) {
		if (this.name == "" || this.name == null || this.name.equals(null) || this.name.equals("")) {
			System.out.println(amount+" 원 입금 됨");
		}else {
			System.out.println(this.name+"님의 이름으로"+amount+" 원 입금 됨");
		}
		balance += amount;
		return balance;
	}
	
	//출금
	public int withdraw(int amount) {
		if (this.balance-amount <= 0) {
			System.out.println("출금 잔액이 부족합니다!!");
		}else {
			if (this.name == "" || this.name == null || this.name.equals(null) || this.name.equals("")) {
				System.out.println(amount+" 원 출금 됨");
			}else {
				System.out.println(this.name+"님의 이름으로"+amount+" 원 출금 됨");
			}
			balance -= amount;
		}
		return balance;
	}
	
	//잔액조회
	public int checkMyBalance() {
		
		if (this.name == "" || this.name == null || this.name.equals(null) || this.name.equals("")) {
			System.out.println("현재 남은 잔액 : "+balance);
		}else {
			System.out.println(this.name+"님의 현재 남은 잔액 : "+balance);
		}
		
		return balance;
	}
}