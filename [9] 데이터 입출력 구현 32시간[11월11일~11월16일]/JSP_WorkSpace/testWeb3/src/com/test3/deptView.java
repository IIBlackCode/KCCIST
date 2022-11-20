package com.test3;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/deptView")
public class deptView extends HttpServlet {

	protected void doGet(HttpServletRequest request, 
			HttpServletResponse response) throws ServletException, IOException {
			String dept_id = request.getParameter("DEPT_ID");
		try {
			Connection conn = DbConnection.getConnection();
			PreparedStatement ps = 
					conn.prepareStatement("SELECT * FROM dept WHERE dept_id = ?");
			ps.setString(1, dept_id);
			ResultSet rs = ps.executeQuery();
			response.setContentType("text/html;charset=utf-8");
			PrintWriter pw = response.getWriter();
			pw.println("<html><body>");
			pw.println("<table border=1>");		
			if(rs.next()) {
				pw.println("<tr>");
				pw.println("<td>부서번호</td>");
				pw.println("<td>" + rs.getInt("DEPT_ID") + "</td>");
				pw.println("</tr><tr>");
				pw.println("<td>부서명</td>");
				pw.println("<td>" + rs.getString("DEPT_NAME") + "</td>");
				pw.println("</tr><tr>");
				pw.println("<td>위치</td>");
				pw.println("<td>" + rs.getInt("LOC_ID") + "</td>");
				pw.println("</tr>");
			}
			rs.close();
			pw.println("</table>");	
			pw.println("<a href='deptUpdate?DEPT_ID=" + dept_id + "'>수정</a>");
			pw.println("<a href='deptDelete?DEPT_ID=" + dept_id + "'>삭제</a>");
			pw.println("<a href='deptList'>목록</a>");
			pw.println("</body></html>");
			pw.close();
			conn.close();
			} catch (ClassNotFoundException | SQLException e) {
				
				e.printStackTrace();
				System.out.println(e);
			}
		}

}
