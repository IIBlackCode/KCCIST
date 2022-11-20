package QUIZE.Workshop._1;

import java.util.Scanner;

// 문제 1.
// 커피 주문을 하려고 한다.
// 메뉴를 보고, 각 메뉴 별로 몇 개씩 주문할 것인지 입력 받아 지불해야 할 총 금액을 계산해 보자.
// 그리고 총 금액이 일정 금액을 넘어서면 포인트를 적립해 준다.
// 총 금액 12000원 이상 : 구매 금액의 1% 적립
// 총 금액 30000원 이상 : 구매 금액의 2% 적립
public class Workshop01 {
    
    public static void main( String[] args ) {
        
        System.out.println( "========= 메뉴 =========" );
        System.out.println( " 1. 아메리카노   2000원" );
        System.out.println( " 2. 카페라떼   3000원" );
        System.out.println( " 3. 베이글   1500원" );
        System.out.println( " 4. 크림치즈   500원" );
        
        int sum = getUserInput();
        int point = 0;
        if (sum >= 12000 && sum < 30000) {
//			point = (float) (sum*0.01);
			point = (int) (sum*0.01);
			System.out.println("포인트 적립 : "+point+"점");
		}else if(sum >= 30000){
			point = (int) (sum*0.02);
			System.out.println("포인트 적립 : "+point+"점");
			
		}
        
    }//The end of Main method
    
    public static int getUserInput() {
        int sum = 0;
    	@SuppressWarnings("resource")
		Scanner scanner = new Scanner(System.in);
    	System.out.println("========= 주문 =========");
    	System.out.print( " 아메리카노 주문 수량 : " );
    	int value1 = scanner.nextInt();
    	System.out.print( " 카페라떼 주문 수량 : " );
    	int value2 = scanner.nextInt();
    	System.out.print( " 베이글 주문 수량 : " );
    	int value3 = scanner.nextInt();
    	System.out.print( " 크림치즈 주문 수량 : " );
    	int value4 = scanner.nextInt();
    	
    	System.out.println("========= 금액 =========");
    	System.out.println("아메리카노 : "+(value1*2000)+"원");
    	System.out.println("라떼 : "+(value2*3000)+"원");
    	System.out.println("베이글 : "+(value3*1500)+"원");
    	System.out.println("크림치즈 : "+(value4*500)+"원");
    	
    	System.out.println("=======================");
    	sum = (value1*2000)+(value2*3000)+(value3*1500)+(value4*500);
    	System.out.println("총 구매 금액 : "+sum);
    	
    	/*
    	if (sum >= 12000 && sum < 30000) {
//			point = (float) (sum*0.01);
			point = (int) (sum*0.01);
			System.out.println("포인트 적립 :"+point);
		}else if(sum >= 30000){
			point = (int) (sum*0.02);
			System.out.println("포인트 적립 :"+point);
			
		}*/
    	
    	return sum;
    	
    }//The end of getUserInput
}// The end of class
