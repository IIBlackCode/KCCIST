package JAVA수업._20200914.TEST11.com.test01;

class Student_Instance {
	public String name;
	
	
	
	public String getName() {
		return name;
	}



	public void setName(String name) {
		this.name = name;
	}



	public void gotoSchool() {
		System.out.println(this.name +"이 학교에 가다");
	}
	
}

class Student_Static {
	public static String name;
	
	
	
	public static String getName() {
		return name;
	}
	
	
	
	public static void setName(String nm) {
		name = nm;
	}
	
	
	
	public static void gotoSchool() {
		System.out.println(name +"이 학교에 가다");
	}
	
}

class Employee {
	private String name;
	
	public Employee() {
	}
	public Employee(String name) {
		super();
		this.name = name;
	}
	public void work() {
		System.out.println(this.name + "이 일을 한다.");
	}

	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
}

public class Test01 {
	
	public static void main(String[] args) {
		Student_Instance stu = new Student_Instance();
		stu.setName("홍길동[Instance]");
		stu.gotoSchool();
		
		Student_Static.setName("홍길동[Static]");		
		Student_Static.gotoSchool();	
		
		Employee emp = new Employee("이순신");
		System.out.println(emp.getName());
		emp.work();
	}

}
