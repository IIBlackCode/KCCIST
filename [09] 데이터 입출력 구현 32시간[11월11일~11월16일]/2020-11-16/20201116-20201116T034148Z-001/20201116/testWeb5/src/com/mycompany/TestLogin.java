package com.mycompany;

public class TestLogin {

	public static void main(String[] args) {
		Login login = EmployeeDao.getPoItemByNo(11112);
		System.out.println(login.getName());
		

	}

}
