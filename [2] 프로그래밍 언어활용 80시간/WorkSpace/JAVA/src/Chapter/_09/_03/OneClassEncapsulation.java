package Chapter._09._03;

class SinusCap {
	void sniTake() {
		System.out.println("Äà¹°ÀÌ ½Ï~ ³³´Ï´Ù.");
	}
	void sneTake() {
		System.out.println("ÀçÃ¤±â°¡ ¸Ü½À´Ï´Ù.");
	}
	void snuTake() {
		System.out.println("ÄÚ°¡ »½ ¶Õ¸³´Ï´Ù.");
	}
	
	void take() {
		sniTake();
		sneTake();
		snuTake();
	}
}

class ColdPatient2 {
	void takeSinus(SinusCap cap) {
		cap.take();
	}
}


public class OneClassEncapsulation {
	public static void main(String[] args) {
		ColdPatient2 suf = new ColdPatient2();
		suf.takeSinus(new SinusCap());
	}
}
