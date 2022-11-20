package QUIZE.Workshop._2._4;

import java.util.Scanner;

public class Quize3 {
	public static void main(String[] args) {

		int score = 0;
		int sum = 0;
		Scanner scan = new Scanner(System.in);
		                                                         
		String[] StudentScore1 = {"A","B","A","C","C","D","E","F","A","D"};
		String[] StudentScore2 = {"D","B","A","B","C","A","E","F","A","D"};
		String[] StudentScore3 = {"E","D","D","A","C","B","E","E","A","D"};
		String[] StudentScore4 = {"C","B","A","E","D","D","E","F","A","D"};
		String[] StudentScore5 = {"A","B","D","C","C","D","E","E","A","D"};
		
		scoreCount(StudentScore1);
		scoreCount(StudentScore2);
		scoreCount(StudentScore3);
		scoreCount(StudentScore4);
		scoreCount(StudentScore5);

	}
	
	private static int scoreCount(String[] studentScore) {
		String[] answer = {"D","B","D","C","C","D","A","E","A","D"};
		Student student5 = new Student(studentScore);
		int score = 0;
		for (int i = 0; i < answer.length; i++) {
			if (answer[i].equals(student5.student[i])) {
				score++;
			}
		}
		System.out.println(student5.studentNum+"번째 학생의 정답 갯수 :"+score+"/10, "+(score)*10+"점");

		return score;
	}

}
