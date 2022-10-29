package QUIZE.Workshop._2._3;

/*
 * SubscriberTest실행 클래스의 형태를 보고 생성자를 포함하는 클래스를 정의해보라. 
 */
public class SubscriberInfoTest { 
	public static void main(String[] args) { 
		SubscriberInfo obj1, obj2,obj3; 
		obj1=new SubscriberInfo("박유신","1017db","daewi"); 
		obj2=new SubscriberInfo("백곰","baekom","white", "200-000-0000","north pole"); 
		obj3=new SubscriberInfo(); 
		printSubscriberInfo(obj1); 
		printSubscriberInfo(obj2); 
		printSubscriberInfo(obj3); 
		obj1.setAddress("교직원1숙사"); 
		obj1.setPhoneNo("133-1234-5678"); 
		printSubscriberInfo(obj1); 
	} 
	static void printSubscriberInfo(SubscriberInfo obj){ 
		//아래 변수는 인스턴스 접근방식으로 접근 가능 > public이라는 의미
		System.out.println("이름:"+obj.name); 
		System.out.println("아이디:"+obj.id); 
		System.out.println("패스워드:"+obj.password); 
		System.out.println("전화번호:"+obj.phoneNo); 
		System.out.println("주소:"+obj.address); 
		System.out.println(); 
	} 
}