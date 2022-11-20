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

@WebServlet("/deptDelete")
public class deptDelete extends HttpServlet {

	protected void doGet(HttpServletRequest request,
			HttpServletResponse response) throws ServletException, IOException {
	// DELETE FROM dept WHERE dept_id = ?		
		try {
			request.setCharacterEncoding("UTF-8");
			String deptId = request.getParameter("DEPT_ID");
		
			Connection conn = DbConnection.getConnection();
			PreparedStatement ps = 
					conn.prepareStatement("DELETE FROM dept WHERE dept_id = ?");
			ps.setInt(1, Integer.parseInt(deptId));
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
