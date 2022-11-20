package com.test2;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.sql.*;
@WebServlet("/MyTestDatabase")
public class MyTestDatabase extends HttpServlet {

	@Override
	protected void doGet(HttpServletRequest req, 
			HttpServletResponse resp) throws ServletException, IOException {
		try {
Class.forName("oracle.jdbc.driver.OracleDriver");
Connection conn = 
DriverManager.getConnection("jdbc:oracle:thin:@10.10.14.125:1521:company","scott","1234");
// SELECT * FROM dept;
PreparedStatement ps = conn.prepareStatement("SELECT * FROM dept");
ResultSet rs = ps.executeQuery();
resp.setContentType("text/html;charset=utf-8");
PrintWriter pw = resp.getWriter();
pw.println("<html><body>");
while(rs.next()) {
	pw.println(rs.getInt("DEPT_ID") + ",");
	pw.println(rs.getString("DEPT_NAME") + ",");
	pw.println(rs.getInt("LOC_ID") + "<br>");
}
rs.close();
pw.println("</body></html>");
pw.close();
		} catch (ClassNotFoundException | SQLException e) {
	
			e.printStackTrace();
			System.out.println(e);
		}
	}
}




