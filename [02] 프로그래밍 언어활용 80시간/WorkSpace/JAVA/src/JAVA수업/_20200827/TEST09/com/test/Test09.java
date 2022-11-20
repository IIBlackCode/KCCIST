package JAVA¼ö¾÷._20200827.TEST09.com.test;

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
}


public class Test09 {
	
	static void dbopen(DataBase d) {
		d.open();
	}

	
	
	public static void main(String[] args) {
		
		Oracle o = new Oracle();
		o.open();
		o.oracleSelect();
		System.out.println("==============");
		
		DataBase d = o;
		Oracle o2 = (Oracle) d;
		o2.open();
		o2.oracleSelect();
		System.out.println("==============");
		
		Mysql m = new Mysql();
		m.open();
		m.mysqlSelect();
		DataBase d2 = m;
		@SuppressWarnings("unused")
		Mysql m2 = (Mysql) d2;
		System.out.println("==============");
		
		Oracle oracle = new Oracle();
		Mysql mysql = new Mysql();
		dbopen(oracle);
		dbopen(mysql);
		System.out.println("==============");
		
	}

}
