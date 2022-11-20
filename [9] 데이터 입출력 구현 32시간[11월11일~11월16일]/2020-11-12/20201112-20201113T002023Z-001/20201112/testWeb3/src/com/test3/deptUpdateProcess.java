package com.test3;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/deptUpdateProcess")
public class deptUpdateProcess extends HttpServlet {
	protected void doPost(HttpServletRequest request, 
			HttpServletResponse response) throws ServletException, IOException {
		try {
			request.setCharacterEncoding("UTF-8");
			String deptId = request.getParameter("DEPT_ID");
			String deptName = request.getParameter("DEPT_NAME");
			String locId = request.getParameter("LOC_ID");
		
			Connection conn = DbConnection.getConnection();
			PreparedStatement ps = conn.prepareStatement("UPDATE dept SET dept_name = ?, loc_id = ? where dept_id = ?");
			ps.setString(1, deptName);
			ps.setInt(2, Integer.parseInt(locId));
			ps.setInt(3, Integer.parseInt(deptId));
			int ret = ps.executeUpdate();
//			request.getRequestDispatcher("deptList").forward(request, response);
			response.sendRedirect("deptList");
			conn.close();
		} catch (ClassNotFoundException | SQLException e) {
	
			e.printStackTrace();
			System.out.println(e);
		} finally {
			
		}
	}
}
