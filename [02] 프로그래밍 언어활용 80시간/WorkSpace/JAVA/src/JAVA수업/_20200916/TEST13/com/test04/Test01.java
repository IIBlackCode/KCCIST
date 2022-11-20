package JAVA¼ö¾÷._20200916.TEST13.com.test04;

interface Getable<T> {
	public T get();
}

class Box<T> implements Getable<T> {

	@Override
	public T get() {
		// TODO Auto-generated method stub
		return null;
	}
	
}

class Toy {

	@Override
	public String toString() {
		return "Toy";
	}
	
	
}

public class Test01 {

}
