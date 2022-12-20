package com.test;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/Login")
public class Login extends HttpServlet {
	protected void doPost(HttpServletRequest request, 
			HttpServletResponse response) throws ServletException, IOException {

		response.setContentType("text/html;charset=utf-8");
		PrintWriter pw = response.getWriter();
		
		String name = request.getParameter("name");
		if(name.equals("admin")) {
			RequestDispatcher rp = request.getRequestDispatcher("Test");
			rp.forward(request, response);
		} else {
			pw.println("로그인이 실패하였습니다.");
			RequestDispatcher rp = 
					request.getRequestDispatcher("login.html");
			rp.include(request, response);
		}
	}
	
	protected void doGet(HttpServletRequest request, 
			HttpServletResponse response) throws ServletException, IOException {

		response.setContentType("text/html;charset=utf-8");
		PrintWriter pw = response.getWriter();
		
		String name = request.getParameter("name");
		if(name.equals("admin")) {
			RequestDispatcher rp = request.getRequestDispatcher("Test");
			rp.forward(request, response);
		} else {
			pw.println("로그인이 실패하였습니다.");
			RequestDispatcher rp = 
					request.getRequestDispatcher("login.html");
			rp.include(request, response);
		}
	}

}
