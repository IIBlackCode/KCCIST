package JAVA수업._20200826.TEST06.com.test;

public class Employee {
	
	//private 접근불가
	private String name;
	private int age;

	public String name2;
	public int age2;
	
	public String getName2() {
		return name2;
	}
	public void setName2(String name2) {
		this.name2 = name2;
	}
	public int getAge2() {
		return age2;
	}
	public void setAge2(int age2) {
		this.age2 = age2;
	}
	
	@Override
	public String toString() {
		return "Employee [name=" + name + ", age=" + age + ", name2=" + name2 + ", age2=" + age2 + "]";
	}
}
