package example;

interface Printable {
	public void print(String doc);
}
class Printer implements Printable {
	@Override
	public void print(String doc) {  //Printable을 구현하는 Printer 클래스
		System.out.println(doc); // 오버라이딩 관계 성립
	}
}

class PrintableInterface {
	public static void main(String[] args) {
		Printable prn = new Printer();   //Printable형 참조변수 선언 가능
		prn.print("Hello Java");
	}
}