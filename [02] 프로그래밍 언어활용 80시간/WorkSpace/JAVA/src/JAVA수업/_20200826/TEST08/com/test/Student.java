package JAVA수업._20200826.TEST08.com.test;

public class Student {
	
	//클래스 영역 외에서 값 변경을 방지하기 위해 private 선언
	private String name;
	private static String test;
	
	public Student() {
		super();
	}

	public Student(String name) {
		super();
		this.name = name;
//		this.test
	}

	//getter and setter로 변수에 값 저장 가능 
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
	
}
