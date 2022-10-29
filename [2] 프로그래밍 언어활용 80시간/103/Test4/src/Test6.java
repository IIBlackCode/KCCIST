class Student{
	public String name;
	public int age;
	public void setNameAge(String nm, int ag) {
		name = nm;
		age = ag;
	}
}
public class Test6 {
	public static void main(String[] args) {
		Student stu = new Student();
		stu.name = "홍길동";
		stu.age = 20;
stu.setNameAge("강감찬", 50);
System.out.println(stu.name + "," + stu.age);

	}

}
