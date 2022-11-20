package JAVA수업._20200825.TEST04;

public class Test09 {
	public static void main(String[] args) {
		Employee2 defaulContstuctor = new Employee2();
		Employee2 onveloadingContstuctor = new Employee2("강감찬",50);
		
		System.out.println(defaulContstuctor.toString());
		System.out.println(onveloadingContstuctor.toString());
	}
}

class Employee2 {
	public String name;
	public int age;
	
	/*Default Contstuctor*/
	public Employee2() {
		System.out.println("Default Constructor");
		this.name = "이순신";
	}
	/*Overloading Contstuctor*/
	public Employee2(String name, int age) {
		System.out.println("Overloading Contstuctor");
		this.name = name;
		this.age = age;
	}
	
	public void setNameAge(String name, int age) {
		this.name = name;
		this.age = age;
	}
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	@Override
	public String toString() {
		return "Employee2 [name=" + name + ", age=" + age + "]";
	}
	
}