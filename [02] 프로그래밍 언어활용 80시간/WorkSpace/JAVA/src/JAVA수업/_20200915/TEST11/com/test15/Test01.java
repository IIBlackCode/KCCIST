package JAVA¼ö¾÷._20200915.TEST11.com.test15;

class MyInteger {
	
	private int i;
	
	//Default Constructor
	public MyInteger() {
	}
	
	//Constructor
	public MyInteger(int i) {
		this.i = i;
	}
	
	//Getter & Setter
	public int getI() {
		return i;
	}
	public void setI(int i) {
		this.i = i;
	}
	
	//toString
	@Override
	public String toString() {
		System.out.println("MyInteger [\n\t i=" + i + ",\n\t getI()=" + getI() + ",\n\t getClass()=" + getClass() + ",\n\t hashCode()=" + hashCode() + ",\n\t toString()=" + super.toString() + "\n]\n");
		return Integer.toString(i);
	}
	
}

public class Test01 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MyInteger m = new MyInteger(10);
		System.out.println(m);
	}

}
