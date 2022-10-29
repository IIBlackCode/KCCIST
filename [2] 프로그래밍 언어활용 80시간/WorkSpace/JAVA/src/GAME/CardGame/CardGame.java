package GAME.CardGame;

import java.util.Scanner;

class CardGame {
	
	@SuppressWarnings("resource")
	void takeTheCard() {
		int sum = 0;

		int[] card1 = {1,3,5,7,9,11,13,15};
		int[] card2 = {2,3,6,7,10,11,14,15};
		int[] card3 = {4,5,6,7,12,13,14,15};
		int[] card4 = {8,9,10,11,12,13,14,15};
		
		
		Scanner scan = new Scanner(System.in);
		
		while(true) {
			
			System.out.print("카드게임을 시작하시겠습니까? [시작 : y, 종료 : 0]:");
			String gameStart = scan.nextLine();
			
			if (gameStart.equals("y")||gameStart.equals("Y")) {
				System.out.println("1~15중 숫자 하나를 고르시오");
				
				cardDeck(card1,1);
				System.out.print("1. 생각하신 카드가 있나요? :");
				String choice1 = scan.nextLine();
				if (choice1.equals("y")||choice1.equals("Y")) {
					sum = 1;
				}
				
				cardDeck(card2,2);
				System.out.print("2. 생각하신 카드가 있나요? :");
				String choice2 = scan.nextLine();
				
				if (choice2.equals("y")||choice2.equals("Y")) {
					sum = sum+2;
				}
				
				cardDeck(card3,3);
				System.out.print("3. 생각하신 카드가 있나요? :");
				String choice3 = scan.nextLine();
				
				if (choice3.equals("y")||choice3.equals("Y")) {
					sum = sum+4;
				}
				
				cardDeck(card4,4);
				System.out.print("4. 생각하신 카드가 있나요? :");
				String choice4 = scan.nextLine();
				
				if (choice4.equals("y")||choice4.equals("Y")) {
					sum = sum+8;
				}
				
				System.out.println("생각하신 카드는 ["+sum+"] 입니다.");
			}else if(gameStart.equals("0")) {
				System.out.println("게임을 종료합니다.");
				break;
			}
		}
		
	}
	
	void cardDeck (int[] card, int num) {
		
		int temp = 0;
		int randomNum = 0;

		for (int i = 0; i < card.length; i++) {
			randomNum = (int)(Math.random()*card.length);
			temp = card[i];
			card[i] =card[randomNum];
			card[randomNum] = temp;
		}
		
		System.out.println("\t\t\t\t**  "+num+"번째 카드  **");
		System.out.println("\t\t\t\t******************");
		for (int i = 0; i < card.length; i++) {
			System.out.println("\t\t\t\t**\t["+card[i]+"]\t**");
		}
		
		//향상된 포문
		/*
		for (int i : card) {
			System.out.println("\t\t\t\t**\t["+card[i]+"]\t**");
		}
		 */
		System.out.println("\t\t\t\t******************");
		System.out.println("");
	}// end of method
}