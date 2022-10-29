package Chapter._21._1;

class Apple {
	public String toString() {
		return "I am an apple.";
	}
}

class Orange {
	public String toString() {
		return "I am an Orange.";
	}
}

class AppleBox {
	private Apple ap;

	public Apple getAp() {
		System.out.println("take out an apple");
		return ap;
	}

	public void setAp(Apple ap) {
		System.out.println("put in an apple");
		this.ap = ap;
	}
}

class OrangeBox {
	private Orange or;

	public Orange getOr() {
		System.out.println("take out an Orange");
		return or;
	}

	public void setOr(Orange or) {
		System.out.println("put in an Orange");
		this.or = or;
	}
}


public class FruitAndBox {
	public static void main(String[] args) {
		System.out.println("make the AppleBox");
		AppleBox aBox = new AppleBox();
		System.out.println("make the OrangeBox");
		OrangeBox oBox = new OrangeBox();
		
		aBox.setAp(new Apple());
		oBox.setOr(new Orange());
		
		Apple ap = aBox.getAp();
		Orange or = oBox.getOr();
		
		System.out.println(ap);
		System.out.println(or);
	}
}
