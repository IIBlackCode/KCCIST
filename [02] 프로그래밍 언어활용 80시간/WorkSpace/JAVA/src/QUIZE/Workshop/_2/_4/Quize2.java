package QUIZE.Workshop._2._4;

import java.util.Scanner;

/*class Student {
	static int studentNum;
	String [] student;
	public Student(String[] student) {
		studentNum++;
		this.student = student;
		System.out.print(studentNum + "번째 학생의 답 : ");
		for (int i = 0; i < student.length; i++) {
			System.out.print("["+student[i]+"]");
		}
		System.out.println("");
		
	}
}*/

public class Quize2 {
	public static void main(String[] args) {

		int score = 0;
		int sum = 0;
		String[] answer = {"D","B","D","C","C","D","A","E","A","D"};
		Scanner scan = new Scanner(System.in);
		                                                         
		String[] StudentScore1 = {"A","B","A","C","C","D","E","F","A","D"};
		String[] StudentScore2 = {"D","B","A","B","C","A","E","F","A","D"};
		String[] StudentScore3 = {"E","D","D","A","C","B","E","E","A","D"};
		String[] StudentScore4 = {"C","B","A","E","D","D","E","F","A","D"};
		String[] StudentScore5 = {"A","B","D","C","C","D","E","E","A","D"};
		
		Student student1 = new Student(StudentScore1);
		for (int i = 0; i < answer.length; i++) {
			if (answer[i].equals(student1.student[i])) {
				score++;
			}
		}
		System.out.println(student1.studentNum+"번째 학생의 정답 갯수 :"+score);
		score =0;
		
		Student student2 = new Student(StudentScore2);
		for (int i = 0; i < answer.length; i++) {
			if (answer[i].equals(student2.student[i])) {
				score++;
			}
		}
		System.out.println(student2.studentNum+"번째 학생의 정답 갯수 :"+score);
		score =0;
		
		Student student3 = new Student(StudentScore3);
		for (int i = 0; i < answer.length; i++) {
			if (answer[i].equals(student3.student[i])) {
				score++;
			}
		}
		System.out.println(student3.studentNum+"번째 학생의 정답 갯수 :"+score);
		score =0;
		
		Student student4 = new Student(StudentScore4);
		for (int i = 0; i < answer.length; i++) {
			if (answer[i].equals(student4.student[i])) {
				score++;
			}
		}
		System.out.println(student4.studentNum+"번째 학생의 정답 갯수 :"+score);
		score =0;
		
		Student student5 = new Student(StudentScore5);
		for (int i = 0; i < answer.length; i++) {
			if (answer[i].equals(student5.student[i])) {
				score++;
			}
		}
		System.out.println(student5.studentNum+"번째 학생의 정답 갯수 :"+score);
		score =0;

	}

}
