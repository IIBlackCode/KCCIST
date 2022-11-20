package test1;

public class test3 {

public static void main(String[] args) {
	int a = 100;
	int b = 200;
	int c = a + b;
	int d = c;
	Employee e = new Employee();
	e.empno = "A001";
	String empno2 = e.empno;
	System.out.println(empno2);
	}
}

class Employee {
	 public String empno;
	 
}