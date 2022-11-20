package Chapter._20._3;

import java.util.Random;
/*
 * 난수(Random Number)의 생성
 * 가짜 난수(Pseudo random number)
 */
public class PseudoRandom {
	public static void main(String[] args) {
		
		//생성자에 전달된 숫자(Seed Number, 시드값)는 난수의 생성 과정에서 씨앗으로 사용
		//난수생성 알고리즘이 이 숫자를 기반으로 돌아가기 때문에 난수패턴은 100% 일치, 결과동일
		Random rand = new Random(12);
		
		for (int i = 0; i < 7; i++) {
			// 0이상 1000미만 난수 생성, 중복있음
			System.out.println(rand.nextInt(1000));
		} 
		
		System.out.println(System.currentTimeMillis());
	}
}
