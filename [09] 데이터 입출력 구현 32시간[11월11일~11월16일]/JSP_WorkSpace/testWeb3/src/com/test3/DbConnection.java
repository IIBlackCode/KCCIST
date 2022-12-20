package com.test3;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DbConnection {
	public static Connection getConnection() throws ClassNotFoundException, SQLException {
		Class.forName("oracle.jdbc.driver.OracleDriver");
		Connection conn = 
		DriverManager.getConnection("jdbc:oracle:thin:@10.10.14.125:1521:company","scott","1234");
		return conn;
	}
}
