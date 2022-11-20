class Employee {
	public Employee() { // Default Constructor
		name = "이순신";
	}

	public Employee(String nm) { // Overloading Constructor
		name = nm;
	}

	public String name;
}


public class Test8 {
	public static void main(String[] args) {
		// Employee emp = new Employee();
		Employee emp = new Employee("강감찬");
		System.out.println(emp.name);
	}
}
