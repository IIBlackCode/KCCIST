package com.test2;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.http.*;

public class MyServlet2 extends HttpServlet {
	public void doGet(HttpServletRequest req,
			HttpServletResponse res) throws IOException {		
		PrintWriter pw = res.getWriter();
		res.setContentType("text/html");
		pw.println("<html><body>Hello Servlet</body></html>");
		pw.close();
		
	}
}
