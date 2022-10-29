package JAVA¼ö¾÷._20200828.TEST10.com.test09;

interface DataBase {
	void open();
}

class Oracle implements DataBase{

	@Override
	public void open() {
		// TODO Auto-generated method stub
		System.out.println("Oracle open");
	}
}

class MySql implements DataBase {

	@Override
	public void open() {
		// TODO Auto-generated method stub
		System.out.println("MySql open");
	}
}

class MsSql implements DataBase {
	
	@Override
	public void open() {
		// TODO Auto-generated method stub
		System.out.println("MsSql open");
	}
}

public class Test {
	
	static void dbOpen(DataBase db) {
		db.open();
	}
	public static void main(String[] args) {
		DataBase db = new Oracle();
		db.open();
		DataBase db2 = new MySql();
		db2.open();
		System.out.println("======================");
		dbOpen(db);
		dbOpen(db2);
	}
}
