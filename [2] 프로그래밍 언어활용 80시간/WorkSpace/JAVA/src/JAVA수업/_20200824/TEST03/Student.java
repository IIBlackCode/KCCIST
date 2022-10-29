package JAVA수업._20200824.TEST03;
public class Student{
	//public 접근제어자 사용시 값을 저장 및 호출이 가능
	public String name;
	public int age;
	public String gender;
	
	public void study() {
		System.out.println(name + ", "+age+", "+gender+" 공부를 한다.");
	}

	@Override
	public String toString() {
		return "Student [name=" + name + ", age=" + age + ", gender=" + gender + "]";
	}
}