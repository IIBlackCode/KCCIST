package Chapter._17._2;

/*
 * 1. 인터페이스 기능추가 방법
 * 인터페이스 간 상속 지원
 *  - 두 클래스 사이의 상속은 extends로 명시한다.
 *  - 두 인터페이스 사이의 상속도 extends로 명시한다.
 *  - 인터페이스와 클래스 사이의 구현만 implements로 명시한다.
 */

//MS에서 제공하는 Interface
interface MS_Printable3 {
	public void print(String doc);//흑백출력
}

//MS_Printable3인터페이스를 상속하는 인터페이스 [extends] 
interface ColorPrintable extends MS_Printable3 {
	void printCMYK(String doc);
}

//삼성 흑백프린터 드라이버
class Samsung_PrintDriver_Prn909Drv implements ColorPrintable {

	//흑백 출력
	@Override
	public void print(String doc) {
		System.out.println("From MD-909 Black & White ver");
		System.out.println(doc);
	}

	//컬러 출력
	@Override
	public void printCMYK(String doc) {
		System.out.println("From MD-909 CMYK ver");
		System.out.println(doc);
	}
	
}

public class PrinterDriver3 {
	public static void main(String[] args) {
		String myDoc = "This is a report about...";
		ColorPrintable prn = new Samsung_PrintDriver_Prn909Drv();
		prn.print(myDoc);
		System.out.println();
		prn.printCMYK(myDoc);
	}
}
