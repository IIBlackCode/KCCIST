package JAVA수업._20200824.TEST03.Chapter7;
//162 page
public class BankAccountOO {
	public static void main(String[] args) {
		
		//Instance 두개 생성
		BankAccount yoon = new BankAccount("yoon");
		BankAccount park = new BankAccount("park");
		
		//각 인스턴스를 대상으로 예금 진행
		yoon.deposit(5000);
		park.deposit(5000);
		
		//각 인스턴스를 대상으로 출금을 진행
		yoon.withdraw(2000);
		park.withdraw(2000);
		
		//각 인스턴스를 대상으로 잔액을 조회
		yoon.checkMyBalance();
		park.checkMyBalance();
		
	}
}

