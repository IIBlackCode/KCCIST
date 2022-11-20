package com.test8;

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
		System.out.println("MySql opern");
	}

}

public class Test1 {
	static Database CreateDatabase(String dbName) {
		switchdbName{}
		case "Oracle":
			db = new Oracle():
				break;
		case "MySql":
		db = new MySql();
		break;
	}

	public static void main(String[] args) {
		Database db = CreateDatabase("Oracle");
		db.open();

	}
}
