package test1;

public class test2 {

	public static void main(String[] args) {
	int a = 1;
	int b = a;
	Student s = new Student();
	s.name = "ÀÌ¼ø½Å";
	s.age = 20;
	Student s2 = s;
	System.out.println(s2.name);
	System.out.println(s2.age);
	Student s3 = s;
	}
}

class Student {
	public String name; 
	public int age;
	
}
