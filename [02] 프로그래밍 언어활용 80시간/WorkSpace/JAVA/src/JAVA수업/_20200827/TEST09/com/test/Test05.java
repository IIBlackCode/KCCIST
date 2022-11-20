package JAVA수업._20200827.TEST09.com.test;

class Student2 {
	String name;
	public Student2() {
		// TODO Auto-generated constructor stub
//		this.name = "학생";
//		this("너");
		this("너랑"," 내");
	}
	public Student2(String name) {
		this.name = name;
	}
	public Student2(String you, String me) {
		this.name = you.concat(me);
	}
	public void gotoSchool() {
		System.out.println(this.name+"가(이) 학교에 간다.");
	}
}

class MiddleStudent2 extends Student2 {
	public void study() {
		System.out.println("중학생이 공부한다.");
	}
}

public class Test05 {
	public static void main(String[] args) {
		Student2 stu = new Student2();
		stu.gotoSchool();
		Student2 stu2 = new Student2("니");
		stu2.gotoSchool();
		
		MiddleStudent2 mstu = new MiddleStudent2();
		mstu.gotoSchool();
		mstu.name = "중학생";
		mstu.gotoSchool();
		mstu.study();;
	}
}
