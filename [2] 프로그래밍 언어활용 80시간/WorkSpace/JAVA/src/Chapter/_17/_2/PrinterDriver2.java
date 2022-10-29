package Chapter._17._2;
/*
 * 인터페이스에 선언되는 메소드와 변수
 * 	- 인터페이스의 모든 메소드는 public이 선언된것으로 간주
 *  - 변수는 오로지 상수만 가능
 */
//MS에서 제공하는 Interface
interface MS_Printable2 {
	public void print(String doc);//흑백출력
}

//삼성 흑백프린터 드라이버
class Samsung_PrintDriver_Prn204Drv implements MS_Printable2 {

	@Override
	public void print(String doc) {
		System.out.println("From MD-204 Printer");
		System.out.println(doc);
	}
	
}

//LG 흑백프린터 드라이버
class LG_PrintDriver_MD_731 implements MS_Printable2 {

	@Override
	public void print(String doc) {
		System.out.println("From MD-731 Printer");
		System.out.println(doc);
	}
	
}

public class PrinterDriver2 {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String myDoc = "This is a report about...";
		
		MS_Printable2 prn = new Samsung_PrintDriver_Prn204Drv();
		prn.print(myDoc);
		System.out.println();
		
		prn = new LG_PrintDriver_MD_731();
		prn.print(myDoc);
	}

}
