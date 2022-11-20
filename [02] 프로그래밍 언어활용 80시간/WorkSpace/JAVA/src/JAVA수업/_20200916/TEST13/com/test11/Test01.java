package JAVA수업._20200916.TEST13.com.test11;

interface Drawble {
	void draw();
}

public class Test01 {
	public static void main(String[] args) {
		Drawble d = new Drawble() {

			@Override
			public void draw() {
				System.out.println("Draw");
			}
			
		};//inner class
		
		d.draw();
		/*위의 내용을 람다식으로 구현*/
					//생성자의 소괄호
		Drawble d2 = () ->{System.out.println("Draw");};
		d.draw();
		
		
		
	}//the end of main Method
}
