class Student2 {
	public Student2() {
		System.out.println("Default Constructor");
		name = "ȫ�浿";
		age = 30;
	} // default constructor

	public String name;
	public int age;

	public void setNameAge(String nm, int ag) {
		name = nm;
		age = ag;
	}
}

public class Test7 {
	public static void main(String[] args) {
		Student2 stu = new Student2();
		System.out.println(stu.name + "," + stu.age);
	}
}