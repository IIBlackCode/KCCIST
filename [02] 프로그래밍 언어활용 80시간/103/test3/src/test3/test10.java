class Database{
	public String dbName;
	public void open() { System.out.println(dbName + "를 연결 오픈합니다.");}
}
package test3;

public abstract class test10 {
	public static void databaseOpen(Database db) {
		db.open();
	}
	public static void main(String[] args) {
Database oracle = new Database();
oracle.daName = "Oracle 10g";
oracle.open();
Database mysql = new Database)();
mysql.dbName = "MySql 5.7";
	mysql.open();
	databaseOpen(oracle); // Database db = oracle;
	databaseOpen(mysql); // Database db = mysql
	}
}
