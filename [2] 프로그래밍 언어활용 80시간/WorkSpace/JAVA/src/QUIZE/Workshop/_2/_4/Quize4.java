package QUIZE.Workshop._2._4;

import java.util.Scanner;

public class Quize4 {
	static int num;
	public static void main(String[] args) {

		int score = 0;
		int sum = 0;
		Scanner scan = new Scanner(System.in);
		                                            
		String StudentScore1 = "ABACCDEFAD";
		String StudentScore2 = "DBABCAEFAD";
		String StudentScore3 = "EDDACBEEAD";
		String StudentScore4 = "CBAEDDEFAD";
		String StudentScore5 = "ABDCCDEEAD";
		
		scoreCount(StudentScore1);
		scoreCount(StudentScore2);
		scoreCount(StudentScore3);
		scoreCount(StudentScore4);
		scoreCount(StudentScore5);

	}
	
	private static int scoreCount(String studentScore) {
		String answer = "DBDCCDAEAD";
		int score = 0;
		char temp ;
		for (int i = 0; i < answer.length(); i++) {
			temp = answer.charAt(i);
			if (temp == (studentScore.charAt(i))) {
				score++;
			}
		}
		num++;
		System.out.println(num+"번째 학생의 정답 갯수 :"+score);

		return score;
	}

}
