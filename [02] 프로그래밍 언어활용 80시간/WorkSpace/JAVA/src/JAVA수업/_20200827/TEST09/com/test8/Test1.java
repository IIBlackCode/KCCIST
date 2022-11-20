package JAVA¼ö¾÷._20200827.TEST09.com.test8;

class DataBase {
	void open() {
		System.out.println("Database Open");
	}
}

class Oracle extends DataBase {
	void oracleSelect () {
		System.out.println("Oracle Select");
	}
}
class Mysql extends DataBase {
	void mysqlSelect () {
		System.out.println("Mysql Select");
	}
	void open() {
		System.out.println("Mysql Open");
	}
}

public class Test1 {
	DataBase db;
	public DataBase createDatabase(String dataBase) {
		if ((dataBase.equals("Oracle") || dataBase.equals("oracle")) && db instanceof Oracle) {
			db = new Oracle();
		}else if((dataBase.equals("Mysql")||dataBase.equals("mysql"))&& db instanceof Oracle) {
			db = new Mysql();
		}
		/*
		switch (dataBase) {
		case "Oracle":
			db = new Oracle();
			break;
		case "Mysql":
			db = new Mysql();
			break;

		default:
			break;
		}
		*/
		
		return db;
	}
	
	static void openTest(DataBase db) {
		db.open();
	}
	public static void main(String[] args) {
		DataBase db = new DataBase();
		Oracle oracle = new Oracle();
		Mysql mysql = new Mysql();
		
		openTest(db);
		openTest(oracle);
		openTest(mysql);
		
	}
}
