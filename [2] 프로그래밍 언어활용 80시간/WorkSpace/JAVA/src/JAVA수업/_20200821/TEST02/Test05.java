package JAVA수업._20200821.TEST02;
import java.util.Scanner;

/*
 * Chapter 05
 * 실행 흐름의 컨트롤
 * 104Page
 */
public class Test05 {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		@SuppressWarnings("resource")
		Scanner scan = new Scanner(System.in);
		
		System.out.print("점수를 입력 해 주세요 : ");
		int point = scan.nextInt();
		if (point >= 90 && point <= 100) {
			System.out.println(" A");
		} else if (point >= 80 && point < 90) {
			System.out.println(" B");
		} else if (point >= 70 && point < 80) {
			System.out.println(" C");
		} else if (point >= 60 && point < 70) {
			System.out.println(" D");
		} else if (point >= 101 || point <0) {
			System.out.println(" 점수를 잘못 입력하셧습니다.");
		} else {
			System.out.println(" F");
		}
		
		
		System.out.println("조건연산자 사용");
		String grade;
		grade = (point >= 90 && point <= 100) ? "A":"";
		grade = (point >= 80 && point < 90) ? "B":"";
		grade = (point >= 70 && point < 80) ? "C":"";
		grade = (point >= 60 && point < 70) ? "D":"";
		grade = (point >= 101 || point < 60) ? "점수를 잘못 입력하셧습니다.":"";
		System.out.println(grade);
	}
}
