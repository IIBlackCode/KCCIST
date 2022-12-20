package com.mycompany;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/work02/ProfileServlet")
public class ProfileServlet extends HttpServlet {
	protected void doGet(HttpServletRequest request, 
			HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		PrintWriter pw = response.getWriter();
		request.getRequestDispatcher("link.html").include(request, response);
		
		Cookie[] cks = request.getCookies();
		if(cks != null) {
			String name = cks[0].getValue();
			pw.print("<b>당신의 정보 : </b>");
			pw.print(name);
		} else {
			pw.println("다시 로그인 해주세요.");
			request.getRequestDispatcher("login.html").include(request, response);
		}
		pw.close();
	
	}

}
