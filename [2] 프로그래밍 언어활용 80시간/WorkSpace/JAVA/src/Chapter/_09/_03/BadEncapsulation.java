package Chapter._09._03;

public class BadEncapsulation {
	public static void main(String[] args) {
		ColdPatient suf = new ColdPatient();
		
		suf.takeSinivelCap(new SinivelCap());
		suf.takeSneezeCap(new SneezeCap());
		suf.takeSnuffleCap(new SnuffleCap());
		
	}
}

//Äà¹° Ã³Ä¡¿ë Ä¸½¶
class SinivelCap extends Cap{
	@Override
	void take() {
		System.out.println("Äà¹°ÀÌ ½Ï~ ³³´Ï´Ù.");
	}
}

//ÀçÃ¤±â Ã³Ä¡¿ë Ä¸½¶
class SneezeCap extends Cap{
	@Override
	void take() {
		System.out.println("ÀçÃ¤±â°¡ ¸Ü½À´Ï´Ù.");
	}
}

//ÄÚ¸·Èû Ã³Ä¡¿ë Ä¸½¶
class SnuffleCap extends Cap{
	@Override
	void take () {
		System.out.println("ÄÚ°¡ »½ ¶Õ¸³´Ï´Ù.");
	}
}

//ColdPatient : °¨±âÈ¯ÀÚ
class ColdPatient{
	void takeSinivelCap(SinivelCap cap) {
		cap.take();
	}
	void takeSneezeCap(SneezeCap cap) {
		cap.take();
	}
	void takeSnuffleCap(SnuffleCap cap) {
		cap.take();
	}
}