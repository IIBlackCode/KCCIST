package JAVA수업._20200826.TEST08.Quize;

import java.util.Scanner;

public class Quize {
	public static void main(String[] args) {
		
		String[][] student = {
					{"A","B","A","C","C","D","E","F","A","D"},
					{"D","B","A","B","C","A","E","F","A","D"},
					{"E","D","D","A","C","B","E","E","A","D"},
					{"C","B","A","E","D","D","E","F","A","D"},
					{"A","B","D","C","C","D","E","E","A","D"},
					{"A","B","D","C","C","D","E","E","A","D"}
				};
		
		Scanner scan = new Scanner(System.in);
		int sum = 0;
		String[] answer = {"D","B","D","C","C","D","A","E","A","D"};
//		String[] student = new String[9];
//		Student[] student = new Student[9];
		
		
		/*for (int i = 0; i < student.length; i++) {
			System.out.print(i+"번째 답을 입력하시오 :");
			String q = scan.nextLine();
			student[i] = q;
		}*/
		/*
		for (int i = 0; i < student.length; i++) {
			if (answer[i].equals(student[i])) {
				sum =sum+1;
				System.out.println("answer :"+answer[i]+",  student"+student[i]);
			}
		}
		 */
		
		for (int i = 0; i <5; i++) {
			for (int j = 0; j < 10; j++) {
				if (answer[j].equals(student[i][j])) {
					sum = sum + 1;
//					System.out.println("sum : "+sum+", answer :"+answer[j]+", student :"+student[i][j]);
				}
//				System.out.println("sum : "+sum+", answer["+i+"] :"+answer[i]+", student["+i+"]["+j+"] :"+student[i][j]);
			}
			System.out.println("The Student["+(i+1)+"]'s Score is "+sum);
			sum = 0;
		}
	}
}
