package Study;

public class StudyStart {
	public static void main(String[] args) {
		StudyClass 인스턴스 = new StudyClass();
		
		인스턴스.인스턴스변수1="A";
		인스턴스.인스턴스변수2=0;
		
		StudyClass.스테틱변수1="B";
		StudyClass.스테틱변수2=1;
		
		인스턴스.인스턴스메소드();
		StudyClass.스테틱메소드();
		
		System.out.println(인스턴스.인스턴스메소드());
		System.out.println(StudyClass.스테틱메소드());
		
		
	}
}
