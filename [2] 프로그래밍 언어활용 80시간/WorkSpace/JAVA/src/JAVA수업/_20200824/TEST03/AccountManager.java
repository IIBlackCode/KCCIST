package JAVA수업._20200824.TEST03;

import java.util.Scanner;

import JAVA수업._20200824.TEST03.Chapter7.BankAccount;
import JAVA수업._20200824.TEST03.Chapter7.BankAccountOO;

/*
 *	Chapter 07
 *	07-1 클래스의 정의와 인스턴스의 생성
 *	Page : 165
 *
 *	클래스는 변수와 메소드를 함께 묶어서 저장한다.
 */

@SuppressWarnings("unused")
public class AccountManager {
	public static void main(String[] args) {
		
		@SuppressWarnings("resource")
		Scanner scan = new Scanner(System.in);
		BankAccount bankAccount = new BankAccount();

		System.out.print("사용자 성함을 입력해주세요. : ");
		String entername = scan.nextLine();
		bankAccount.name = entername;
		
		while (true) {

			System.out.println("###########계좌 관리############\n# 1. 입금 \n# 2. 출금\n# 3. 잔액 확인\n# 4. 종료\n###############################");
			
			System.out.print("메뉴 항목을 선택해주세요. : ");
			int choice = scan.nextInt();
			
			if (choice == 1) {
				System.out.print("입금할 금액을 입력해주세요. : ");
				int deposit = scan.nextInt();
				bankAccount.deposit(deposit);
			}else if(choice == 2) {
				System.out.print("출금할 금액을 입력해주세요. : ");
				int amount = scan.nextInt();
				bankAccount.withdraw(amount);
			}else if(choice == 3) {
				System.out.println("잔액 : "+bankAccount.balance);
				bankAccount.checkMyBalance();
//				System.out.println("잔액은"+bankAccount.checkMyBalance()+"원 입니다.");
			}else if(choice == 4) {
				break;
			}//end of if
		}//end of while
	
	}//end of method
	
}//end of class