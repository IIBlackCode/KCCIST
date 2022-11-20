package JAVA수업._20200825.TEST04;

public class Test02 {
	public static void main(String[] args) {
		MyClass2 instanceOfMyclass = new MyClass2();
		instanceOfMyclass.message("안녕하세요");
		String message = instanceOfMyclass.message2("반가워요");
		System.out.println(message);
	
	}
}

//같은 패키지 내에 같은 클래스가 있으면 중복에러가 발생된다.
class MyClass2 {
	public void message(String msg) {
		System.out.println(msg);
	}
	public String message2(String msg) {
		return msg;
	}
}