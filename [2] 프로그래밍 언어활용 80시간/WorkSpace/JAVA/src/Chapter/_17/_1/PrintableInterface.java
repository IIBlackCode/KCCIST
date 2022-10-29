package Chapter._17._1;
/*
 * Interface : 연결점, 접점, 둘 사이를 연결하는 매개체
 * 	- 구현할 인터페이스를 명시할 때 키워드 Implements 사용
 * 	- 한 클래스에서 둘 이상의 인터페이스 구현 가능
 *  - 상속과 구현은 동시에 가능
 */
interface Printable {
	public void print(String doc);
}

class Printer implements Printable {

	@Override
	public void print(String doc) {
		// TODO Auto-generated method stub
		System.out.println(doc);
	}
	
}

public class PrintableInterface {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Printable printableInterfaceInctance = new Printer();
		
		/*
		 * 클래스의 상속처럼 (부모 클래스의 메소드 호출)
		 * 인터페이스에 정의된 추상 메소드 호출 가능
		 */
		printableInterfaceInctance.print("Hello Java");
	}

}
