package test1;

public class test13 {

	public static void main(String[] args) {
	short num = 10;
	num = (short)(num + 77L); // 형 변환 안하면 컴파일 오류 발생
	int rate = 3;
	rate = (int)(rate * 3.5); // 형 변환 안하면 컴파일 오류 발생
	System.out.println(num);
	System.out.println(rate);
	
	num = 10;
	num += 77; // 형 변환 필요하지 않다.
	rate = 3;
	rate *= 3.5; // 형 변환 필요하지 않다.
	System.out.println(num);
	System.out.println(rate);
// 83p
	}

}
