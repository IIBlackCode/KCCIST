package JAVA수업._20200828.TEST10.com.test08;

class A {

	@Override
	public String toString() {
//		return "toString을 정의하지 않으면 객체의 HashCode를 출력한다.";
		return super.toString();
	}
	
}
class B extends A{
	public String toString() {
		return "반가워요";
	}
}

public class test {

	public static void main(String[] args) {
		A a = new A();
		System.out.println("객체에 대해 Refference type은 Default로 toString을 호출한다. \na:"+a);
		/*
		Object의 Method Overriding
		toString
		public String toString()

		Returns a string representation of the object. 
		In general, the toString method returns a string that"textually represents" this object. 
		The result shouldbe a concise but informative representation that is easy for aperson to read.
		It is recommended that all subclasses override this method. 
		The toString method for class Objectreturns a string consisting of the name of the class of which theobject is an instance, 
		the at-sign character `@', andthe unsigned hexadecimal representation of the hash code of theobject.
		In other words, this method returns a string equal to thevalue of: 

		getClass().getName() + '@' + Integer.toHexString(hashCode())
 
		Returns:a string representation of the object.
		 */
		
		A a2 = new B();
		System.out.println(a2);
	}

}
