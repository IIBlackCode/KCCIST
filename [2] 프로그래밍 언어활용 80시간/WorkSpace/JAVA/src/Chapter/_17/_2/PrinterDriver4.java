package Chapter._17._2;

/*
 * 2. 인터페이스 기능 추가 방법
 * 인터페이스의 디폴트 메소드
 *  - 대대적인 기능보강을 위해 모든 인터페이스에 최소 한개 이상의 추상 메소드를 추가해야할 때
 *  - 인터페이스는 기본적으로 public이 선언된 상태
 *  - default 명시
 */

//MS에서 제공하는 Interface
interface MS_Printable4 {
	public void print(String doc);//흑백출력
	//인터페이스의 디폴트메소드 추가
	default void printCMYK(String doc) {}
}

class Prn731Drv implements MS_Printable4 {
	@Override
	public void print(String doc) {
		System.out.println("From Prn731 printer");
		System.out.println(doc);
	}
}

class Prn909Drv implements MS_Printable4 {
	@Override
	public void print(String doc) {
		System.out.println("From MD-909 Black & White ver");
		System.out.println(doc);
	}
	
	@Override
	public void printCMYK(String doc) {
		System.out.println("From MD-909 CMYK ver");
		MS_Printable4.super.printCMYK(doc);
	}
}

public class PrinterDriver4 {
	public static void main(String[] args) {
		String myDoc = "This is a report about...";
		
		MS_Printable4 prn = new Prn731Drv();
		prn.print(myDoc);
		System.out.println();
		
		MS_Printable4 prn2 = new Prn909Drv();
		prn2.print(myDoc);
		prn2.printCMYK(myDoc);
	}
}
