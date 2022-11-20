package com.mycompany;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
@WebServlet("/work01/EmployeeView")
public class EmployeeView extends HttpServlet {

	@Override
	protected void doGet(HttpServletRequest req, 
			HttpServletResponse resp) throws ServletException, IOException {
	
		resp.setContentType("text/html;charset=utf-8");
		PrintWriter pw = resp.getWriter();
		pw.println("<html><body>");
		pw.println("<h4>[사원 확인]</h4>");
		pw.println("사번 : " + req.getParameter("EMP_NO") + "<br>");	
		pw.println("이름 : " + req.getParameter("EMP_NAME") + "<br>");	
		pw.println("부서 : " + req.getParameter("EMP_DEP") + "<br>");
		pw.println("전화번호 : " + req.getParameter("EMP_PHONE") + "<br>");
		pw.println("등급 : " + req.getParameter("EMP_LEVEL") + "<br>");
		pw.println("</body></html>");
		pw.close();
	}

}
