package JAVA¼ö¾÷._20200914.TEST11.com.test05;

class Database {
	void open() {
		System.out.println("Database open");
	}
}

class Oracle extends Database {
	void open() {
		System.out.println("Oracle open");
	}
}
class MySql extends Database {
	void open() {
		System.out.println("MySql open");
	}
	
}

interface DatabaseInterface {
	void open();
}

class Oracle2 implements DatabaseInterface {
	public void open() {
		System.out.println("Oracle open");
	}
}
class MySql2 implements DatabaseInterface {
	public void open() {
		System.out.println("MySql open");
	}
	
}

abstract class DatabaseAbstract {
	abstract void open();
}

class Oracle3 extends DatabaseAbstract {
	public void open() {
		System.out.println("Oracle open");
	}
}
class MySql3 extends DatabaseAbstract {
	public void open() {
		System.out.println("MySql open");
	}
	
}

public class Test01 {

	public static void main(String[] args) {
		/*
		Database[] dbs = new Database[2];
		dbs[0] = new Oracle();
		dbs[1] = new MySql();
		*/
		Database[] dbs = {new Oracle(), new MySql()};
		for (Database d : dbs) {
			d.open();
		}
	}

}
