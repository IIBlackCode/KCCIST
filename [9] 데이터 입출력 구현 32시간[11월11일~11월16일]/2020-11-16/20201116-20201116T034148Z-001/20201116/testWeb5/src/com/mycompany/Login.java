// Model
package com.mycompany;

public class Login {
	private String name;
	private String password;
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	public boolean validate() {
		Login login = EmployeeDao.getPoItemByNo(Integer.parseInt(name));
		if(login.getName() == null) {
			return false;
		} else {
			return true;
		}
	}
}
