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
@WebServlet("/deptUpdate")
public class deptUpdate extends HttpServlet {
	protected void doGet(HttpServletRequest request, 
			HttpServletResponse response) throws ServletException, IOException {
		try {
			request.setCharacterEncoding("UTF-8");
			String dept_id = request.getParameter("DEPT_ID");
			Connection conn = DbConnection.getConnection();
			PreparedStatement ps = 
					conn.prepareStatement("SELECT * FROM dept WHERE dept_id = ?");
			ps.setString(1, dept_id);
			ResultSet rs = ps.executeQuery();
			response.setContentType("text/html;charset=utf-8");
			PrintWriter pw = response.getWriter();	
			int dept_id2 = 0;
			String dept_name = "";
			int loc_id = 0;
			if(rs.next()) {		
				dept_id2 = rs.getInt("DEPT_ID");				
				dept_name = rs.getString("DEPT_NAME");
				loc_id = rs.getInt("LOC_ID");
			}
			pw.println("<html><body>");
			pw.println("<form action=deptUpdateProcess method=post>");
			pw.println("부서번호 : <input type=text name=DEPT_ID size=4 maxlength=4 value=" + dept_id2 + "><br>");
			pw.println("부서명 : <input type=text name=DEPT_NAME size=30 maxlength=30 value=" + dept_name + "><br>");
			pw.println("위치 : <input type=text name=LOC_ID size=4 maxlength=4 value=" + loc_id + "><br>");
			pw.println("<input type=submit value=저장>&nbsp;");
			pw.println("<input type=reset value=취소>");			
			pw.println("</form>");
			pw.println("</html></body>");
			
			rs.close();	
			pw.close();
			conn.close();
			} catch (ClassNotFoundException | SQLException e) {
				
				e.printStackTrace();
				System.out.println(e);
			}
	
	}
}
