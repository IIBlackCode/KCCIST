package Chapter._20._3;

import java.util.Random;
/*
 * 난수(Random Number)의 생성
 */
public class RandomNumberGenerator {
	public static void main(String[] args) {
		Random rand = new Random();
		
		for (int i = 0; i < 7; i++) {
			// 0이상 1000미만 난수 생성, 중복있음
			System.out.println(rand.nextInt(1000));
		} 
		
	}
}
