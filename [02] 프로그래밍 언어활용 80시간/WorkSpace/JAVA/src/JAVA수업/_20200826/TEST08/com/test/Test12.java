package JAVA수업._20200826.TEST08.com.test;

class Student3{
	String name;
	static String school = "서울고등학교";
}

public class Test12 {
	
	public static void main(String[] args) {
		Student3 student = new Student3();
		student.name = "홍길동";
		System.out.println(student.name + ", " + student.school);
		Student3 student2 = new Student3();
		student2.name = "세종대왕";
		System.out.println(student2.name + ", " + student2.school);
		
		//스테틱 변수에 저장
		student2.school = "부천고등학교";

		System.out.println(student.name + ", " + student.school);
		System.out.println(student2.name + ", " + student2.school);
	}

}
