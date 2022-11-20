package JAVA¼ö¾÷._20200828.TEST10.com.test12;


interface Database {
	void open();
}

class Oracle  implements Database{
	public void open() {
		System.out.println("Oracle open");
		
	}
}

class MySql  implements Database{
	@Override
	public void open() {
		System.out.println("MySql open");
		
	}
}

class MsSql  implements Database{
	@Override
	public void open() {
		System.out.println("MsSql open");
		
	}
}

public class Test {
	static Database CreateDataBase(String dbName) {
		
		Database db = null;
		switch (dbName) {
		case "Oracle":
			db = new Oracle();
			break;
		case "MySql":
			db = new MySql();
			break;
		case "MsSql":
			db = new MsSql();
			break;
			
		default:
			break;
		}
		return db;
	}
	public static void main(String[] args) {
	
		Database db = CreateDataBase("Oracle");
		db.open();
		
		Database db2 = CreateDataBase("MySql");
		db2.open();
		
		Database db3 = CreateDataBase("MsSql");
		db3.open();
		
	}
}
