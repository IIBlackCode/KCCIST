package JAVA수업._20200825.TEST04;

public class Test07 {
	public static void main(String[] args) {
		
		Student2 student2 = new Student2();
		
		System.out.println(student2.toString());
	}
}

class Student2{
	public String name;
	public int age;
	
	/*Instance 생성될 때 자동으로 호출된다.*/
	public Student2() {
		System.out.println("Default Constructor");
		name = "홍길동";
		age = 30;
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
	
	public void setNameAge(String name, int age) {
		this.name = name;
		this.age = age;
	}
	
	@Override
	public String toString() {
		return "Student [name=" + name + ", age=" + age + "]";
	}
	
	
}