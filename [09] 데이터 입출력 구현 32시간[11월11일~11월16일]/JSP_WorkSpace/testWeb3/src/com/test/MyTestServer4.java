package com.test;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Enumeration;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/MyTestServer4")
public class MyTestServer4 extends HttpServlet {
	protected void doGet(HttpServletRequest request, 
			HttpServletResponse response) throws ServletException, IOException {

		response.setContentType("text/html");
		PrintWriter pw = response.getWriter();
		ServletContext context = getServletContext();
		String name = context.getInitParameter("name");
		pw.println(name);
		
		String str = "";
		Enumeration<String> names = context.getInitParameterNames();
		while(names.hasMoreElements()) {
			str = names.nextElement();
			pw.println(context.getInitParameter(str));
		}
		pw.close();			
	}
}





