package JAVA수업._20200824.TEST03;

import java.util.Scanner;

/*
 *	Chapter 07
 *	07-1 클래스의 정의와 인스턴스의 생성
 *	Page : 165
 *
 *	클래스는 변수와 메소드를 함께 묶어서 저장한다.
 */

@SuppressWarnings("unused")
public class Test10 {
	public static void databaseOpen(DataBase db) {
		db.open();
	}
	public static void main(String[] args) {
		
		DataBase oracle = new DataBase();
		oracle.dbName = "Oracle 10g";
		DataBase mysql = new DataBase();
		mysql.dbName = "Mysql 5.7";
		mysql.open();
		databaseOpen(oracle);	//Database db = oracle
		databaseOpen(mysql);	//Database db = mysql
	}//end of method
	
}//end of class