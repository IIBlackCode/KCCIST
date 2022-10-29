package JAVA수업._20200826.TEST08.com.test;

public class Test08 {
	
	public static void main(String[] args) {
		Student2[] stu = new Student2[3];
//		stu[0].setName("홍길동"); // 아직은 타입만 선언된 상태
		
		stu[0] = new Student2();
		stu[1] = new Student2();
		stu[2] = new Student2();
		
		stu[0].setName("이순신");
		stu[1].setName("강감찬");
		stu[2].setName("김민서");
		
		System.out.println(stu[0].getName());
		System.out.println(stu[1].getName());
		System.out.println(stu[2].getName());

	}
}

class Student2{
	private String name;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
	
}