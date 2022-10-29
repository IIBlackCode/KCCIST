package JAVA수업._20200821.TEST02.Workshop;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

// 문제 2.
// A대학의 학기말이 되었다. 각과목별로 성적을 입력 받아 장학금을 받을 학생을 선별하려고 한다.
// 장학금을 받을 수 있는 조건은 아래와 같다.
//   1) 평점이 3.7 이상   2) 각 과목별 성적이 2.5 이상 (한 과목이라도 2.5 미만인 과목이 있다면, 과락으로 장학금 탈락)
@SuppressWarnings("unused")
public class Workshop02 {
    
    public static void main( String[] args ) {
        
    	System.out.println( "==============================" );
     
    	double score = 0;
    	double avg = 0;
    	
       	@SuppressWarnings("resource")
		Scanner scanner = new Scanner(System.in);

       	System.out.print( "Computer Science 성적을 입력하세요 : " );
    	double value1 = scanner.nextDouble();
    	
    	System.out.print( "Java Programming 성적을 입력하세요 : " );
    	double value2 = scanner.nextDouble();
    	
    	System.out.print( "공학수학 성적을 입력하세요 : " );
    	double value3 = scanner.nextDouble();
    	
    	System.out.print( "오페라의 이해 성적을 입력하세요 : " );
    	double value4 = scanner.nextDouble();
    	
    	System.out.print( "배드민턴 성적을 입력하세요 : " );
    	double value5 = scanner.nextDouble();
    	
    	avg = getUserInput(value1,  value2, value3, value4, value5)/5;
    	System.out.println("평점은 "+avg+"점 입니다.");
    	
    	if (avg>=3.7) {
    		if (!(value1 < 2.5 || value2 < 2.5 || value3 < 2.5 || value4 < 2.5 || value5 < 2.5)) {
    			System.out.println("다음 학기 장학금 대상자 입니다.");
    		}
		}//The end of if
    	
    	if (avg>=3.7) {
    		if (value1 >= 2.5 && value2 >= 2.5 && value3 >= 2.5 && value4 >= 2.5 && value5 >= 2.5) {
    			System.out.println("다음 학기 장학금 대상자 입니다.");
    		}
    	}//The end of if
    	
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    public static double getUserInput(double value1, double value2, double value3, double value4, double value5) {
    	double score = 0;
        /*
    	
       	Scanner scanner = new Scanner(System.in);
       	System.out.print( "Computer Science 성적을 입력하세요 : " );
       	
    	double value1 = scanner.nextDouble();
    	
    	System.out.print( "Java Programming 성적을 입력하세요 : " );
    	double value2 = scanner.nextDouble();
    	
    	System.out.print( "공학수학 성적을 입력하세요 : " );
    	double value3 = scanner.nextDouble();
    	
    	System.out.print( "오페라의 이해 성적을 입력하세요 : " );
    	double value4 = scanner.nextDouble();
    	
    	System.out.print( "배드민턴 성적을 입력하세요 : " );
    	double value5 = scanner.nextDouble();
        */
    	
    	System.out.println( "==============================" );
    	score = value1+value2+value3+value4+value5;
    	/*
    	avg = score/5;
    	
    	System.out.println("평점은 "+avg+"점 입니다.");
    	if (avg>=3.7) {
    		if (!(value1 < 2.5 || value2 < 2.5 || value3 < 2.5 || value4 < 2.5 || value5 < 2.5)) {
    			System.out.println("다음 학기 장학금 대상자 입니다.");
    		}
		}//The end of if
    	*/
    	return score;
    	
    }// The end of getUserInput()
}//The end of class
