package JAVA¼ö¾÷._20200916.TEST13.com.test08;

enum Gender {
	MAN(10),WOMAN(20);
	int a;
	private Gender(int a) {
		this.a = a;
	}
}

public class Test01 {

	public static void main(String[] args) {
		
		Gender g = Gender.MAN;
		System.out.println(g + ", "+g.a);
		System.out.println(g.valueOf("MAN").a);
	}

}
