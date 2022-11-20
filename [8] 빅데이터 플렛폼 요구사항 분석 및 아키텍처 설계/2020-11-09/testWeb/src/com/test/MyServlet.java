package com.test;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
// http://localhost:8080/testWeb/MyServlet
public class MyServlet extends HttpServlet {
	public void doGet(HttpServletRequest req,
		HttpServletResponse res) throws IOException{
		res.setContentType("text/html");
		PrintWriter pw = res.getWriter();
		pw.println("<html><body>");
		pw.println("Hello Servlet");
		pw.println("</body></html>");
		pw.close();			
	}	
}
