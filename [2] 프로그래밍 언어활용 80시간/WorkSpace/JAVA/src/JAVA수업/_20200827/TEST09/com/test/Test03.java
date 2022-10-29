package JAVA수업._20200827.TEST09.com.test;

class Student {
	String name;
	public Student () {
		this("홍길동");
		eat();
	}
	public Student(String name) {
		this.name = name;
	}
	
	public void study () {
		System.out.println(this.name + "이 공부한다");
	}
	
	public void eat () {
		System.out.println(this.name + "이 밥을 먹는다");
	}
}

public class Test03 {
	public static void main(String[] args) {
		@SuppressWarnings("unused")
		Student stu = new Student();
		Student stu2 = new Student("세종대왕");
		stu2.eat();
	}
}
