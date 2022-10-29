package QUIZE.Workshop._2._4;
class Student {
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
}