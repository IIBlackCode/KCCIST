package JAVA수업._20200914.TEST11.com.test13;

class Employee {
	
	private String name;
	public Employee(String name) {
		this.name = name;
	}
	
	public boolean equals(Object obj) {
		
		if (this.name == ((Employee)obj).name) {
			System.out.println(this.name + ", "+((Employee)obj).name);
			return true;
		}else {
			System.out.println(this.name + ", "+((Employee)obj).name);
			return false;
		}
		
	}
	
}

public class Test01 {
	public static void main(String[] args) {
		Employee emp = new Employee("이순신");
		Employee emp2 = new Employee("홍길동");
		
		if (emp.equals(emp2)) {
			System.out.println("이름이 일치합니다.");
		} else {
			System.out.println("이름이 일치하지 않습니다.");
		}
		
	}
}
