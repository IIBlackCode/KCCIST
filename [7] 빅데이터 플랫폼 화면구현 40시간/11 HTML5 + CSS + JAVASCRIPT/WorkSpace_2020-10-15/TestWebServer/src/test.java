
public class test {
	public static void main(String[] args) {
		System.out.println(startOz("oz"));
	}

	public static String startOz(String str) {
		System.out.println(str.length());
		String result = "";
		if (str.length() > 4) {
			result = str.substring(0, 2);
		} else if (str.length() == 4) {
			result = str.substring(1, 2);
		} else if (str.length() < 4) {
			result = str.substring(0, 1);
		}
		return result;
	}
}
