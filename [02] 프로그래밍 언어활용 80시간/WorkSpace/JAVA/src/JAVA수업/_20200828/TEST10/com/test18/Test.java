package JAVA수업._20200828.TEST10.com.test18;

/*
 * 추상클래스
 * 	인스턴스화 불가능
 */
abstract class Database {
	abstract void open();
	void close() {
		System.out.println("Database close");
	}
}

class Oracle extends Database {
	
	//Database 클래스의 메소드 재정의
	@Override // 바인딩
	void open() {
		System.out.println("Oracle open");
	}
}

class MySql extends Database {
	void open() {
		System.out.println("MySql open");
	}
}

public class Test {
	public static void main(String[] args) {
		Database db = new Oracle();	// Override : 바인딩
		db.open();
		db.close();
		Database db2 = new MySql();	// Override : 바인딩
		db2.open();
		db2.close();
	}
}
