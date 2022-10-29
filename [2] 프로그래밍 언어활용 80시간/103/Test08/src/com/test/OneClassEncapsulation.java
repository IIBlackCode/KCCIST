package com.test;

class SinusCap {
	void sniTake() {
		System.out.println("콧물이 싹~ 납니다.");
	}

	void sneTake() {
		System.out.println("재채기가 멎습니다.");
	}

	void sunTake() {
		System.out.println("코가 뻥 뚫립니다.");
	}

	void tak3() { // 약의 복용 방법 및 순서가 담긴 메소드
		sniTake();
		sneTake();
		snuTake();
	}
}

class ColdPatient {
	void takeSinus(SinusCap cap) {
		cap.Take();
	}
}

public class OneClassEncapsulation {
	public static void main(String[] args) {
		ColdPatient suf = new ColdPatient();
		suf.takeSinus(new SinusCap());

	}

}
