package JAVA¼ö¾÷._20200828.TEST10.com.test04;

class DataBase{
	String open() {
		System.out.println("**\t[DataBase Class, open Method]" +"\n"+"**\tDatabase open\t**");
		return "**\t[DataBase Class, open Method]" +"\n"+"**\tDatabase open\t**";
	}
}

class Oracle extends DataBase{
	String open() {
		super.open();
		return "[Oracle Class, open Method]"+"\n"+"**\tOracle open\t**";
	}
}

class MySql extends DataBase{
	String open() {
		super.open();
		return "[MySql Class, open Method]" + "\n" + "**\tMySql open\t**";
	}
}

public class Test {
	
	static String dbOpen(DataBase db) {
		return db.open();
	}
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.println("=================================");
		System.out.println("[Main] DataBase oracle = new Oracle();");
		DataBase oracle = new Oracle();
		System.out.println("[Main] oracle.open(); : "+ oracle.open());
		System.out.println("=================================");
		System.out.println("[Main] DataBase mysql = new MySql();");
		DataBase mysql = new MySql();
		System.out.println("[Main] mysql.open(); : " + mysql.open());
		System.out.println("=================================");
		dbOpen(new Oracle());
		dbOpen(new MySql());
	}

}
