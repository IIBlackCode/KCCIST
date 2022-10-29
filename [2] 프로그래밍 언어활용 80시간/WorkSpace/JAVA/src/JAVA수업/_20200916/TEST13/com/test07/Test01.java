package JAVA¼ö¾÷._20200916.TEST13.com.test07;



public class Test01 {
	public enum Season {
		WINTER(100), SPRING(200), SUMMER(300), FALL(400);
		private int value;
		Season(int value) {
			this.value = value;
		}
	}
	/*
	public enum Season {
		WINTER(100), SPRING(200), SUMMER(300), FALL(400)
	}
	*/
	public static void main(String[] args) {
		Season s = Season.WINTER;
		System.out.println(s);
		System.out.println("============");
		for (Season s2:Season.values()) {
			System.out.println(s2+ ",\t"+s2.value);
		}
		System.out.println("============");
		System.out.println("Season.valueOf(\"WINTER\") \t\t: "+Season.valueOf("WINTER"));
		System.out.println("Season.valueOf(\"WINTER\").ordinal() \t: "+Season.valueOf("WINTER").ordinal());
		System.out.println("============");
	}
	
}
