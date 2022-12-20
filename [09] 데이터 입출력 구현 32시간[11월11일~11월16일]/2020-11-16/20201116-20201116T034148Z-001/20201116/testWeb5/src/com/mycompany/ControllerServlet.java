// Controller
package com.mycompany;
import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
@WebServlet("/ControllerServlet")
public class ControllerServlet extends HttpServlet {
	protected void doPost(HttpServletRequest request, 
			HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		PrintWriter pw = response.getWriter();
		request.setCharacterEncoding("utf-8");
		String name = request.getParameter("name");
		String password = request.getParameter("password");
		
		Login login = new Login();
		login.setName(name);
		login.setPassword(password);
		
		request.setAttribute("login", login);	
		boolean status = login.validate();
		
		if(status) {
			request.getRequestDispatcher("login_sucess.jsp")
				.forward(request, response);;
		} else {
			request.getRequestDispatcher("login_error.jsp")
				.forward(request, response);
		}		
	}
}





