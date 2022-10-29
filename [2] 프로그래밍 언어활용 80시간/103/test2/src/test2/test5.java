package test2;

import java.util.Scanner;

public class test5 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("점수를 입력해주세요. : ");
int score = sc.nextInt();
if(score <= 100 && score >=90) {
	System.out.println("A 학점 입니다.");
}else if (score < 90 && score >= 80 ) {
	System.out.println("B 학점 입니다.");
}else if (score < 80 && score >= 70) {
	System.out.println("C 학점 입니다.");
	}else if(score < 70 && score >= 60) {
System.out.println("D 학점 입니다.");
	}else if(score <60){
	System.out.println("F 학점입니다.");	
// A : 90<=점수<=100
// B : 80<=점수<90
// C : 70<=점수<80
// D : 60<=점수<70
// F : 60 이하

	}
}
}