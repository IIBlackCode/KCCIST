package Chapter._09._03;

class SinusCap2 {

	SinivelCap siCap = new SinivelCap();
	SneezeCap szCap = new SneezeCap();
	SnuffleCap sfCap = new SnuffleCap();
	
	void take() {
		siCap.take();
		szCap.take();
		sfCap.take();
	}
}

class ColdPatient3 {
	void  takeSinus(SinusCap2 cap) {
		cap.take();
	}
}

public class CompEncapsulation {
	public static void main(String[] args) {
		ColdPatient3 suf = new ColdPatient3();
		suf.takeSinus(new SinusCap2());
	}
}
