package Chapter._17._1;
/*
 * Interface의 본질적 의미
 * 	- 인터페이스 하나를 만들어 모든 업체에 제공
 * 	- 하나하나 일일이 구현할 수 없을 때 인터페이스 하나를 두어 각자 구현할 수 있도록 하기 위함
 */
//MS에서 제공하는 Interface
interface MS_Printable1 {
	public void print(String doc);
}

class Samsung_PrintDriver1 implements MS_Printable1 {

	@Override
	public void print(String doc) {
		System.out.println("From Samsung Printer");
		System.out.println(doc);
	}
	
}

class LG_PrintDriver1 implements MS_Printable1 {

	@Override
	public void print(String doc) {
		System.out.println("From LG Printer");
		System.out.println(doc);
	}
	
}

public class PrinterDriver {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String myDoc = "This is a report about...";
		
		//삼성 프린터 출력
		MS_Printable1 prn = new Samsung_PrintDriver1();
		prn.print(myDoc);
		System.out.println();
		
		//삼성 프린터 출력
		prn = new LG_PrintDriver1();
		prn.print(myDoc);
	}

}
