package example;

interface Printable {
	void print(String doc);
}
class Prn204Drv implements Printable {
	@Override
	public void print(String doc) {
		System.out.println("From MD-204 printer");
		System.out.println(doc);
	}
}

class Prn731Drv implements Printable {
	@Override 
	public void print(String doc) {
		System.out.println("From MD-731 printer");
		System.out.println(doc);
	}
}

class PrinterDriver2


public class PrinterDriver2 {

	public static void main(String[] args) {


	}

}
