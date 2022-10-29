package JAVA수업._20200914.TEST11.com.test11;

@SuppressWarnings("serial")
class CheckAgeException extends Exception {
	public CheckAgeException() {
		super("당신의 나이는 20살 이상입니다.");
	}
}

public class Test01 {
	
	//예외처리를 호출한쪽으로 넘김
	public static void validate(int age) throws CheckAgeException{
		if (age >20) {
			throw new CheckAgeException();
		}else {
			System.out.println("문제없음");
		}
	}
	
	public static void main(String[] args) {
		
		try {
			validate(30);
		} catch (CheckAgeException e) {
			// TODO Auto-generated catch block
			System.out.println("오류 발생 : " + e.getMessage());
		}
		
	}

}
