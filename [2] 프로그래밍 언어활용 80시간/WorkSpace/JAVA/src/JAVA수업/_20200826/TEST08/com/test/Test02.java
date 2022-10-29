package JAVA¼ö¾÷._20200826.TEST08.com.test;

public class Test02 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

class Employee{
	private String name;
	private int age;

	public Employee() {
		this("È«±æµ¿", 20);
	}

	public Employee(String name, int age) {
		this.name = name;
		this.age = age;
	}


	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
	
}
