package com.mycompany;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;


@WebServlet("/work02/LoginServlet")
public class LoginServlet extends HttpServlet {

	@Override
	protected void doPost(HttpServletRequest req, 
			HttpServletResponse resp) throws ServletException, IOException {
		resp.setContentType("text/html;charset=utf-8");
		PrintWriter pw = resp.getWriter();
		req.getRequestDispatcher("link.html").include(req, resp);
		
		String name = req.getParameter("name");
		String password = req.getParameter("password");
		if(password.equals("1234") && name.equals("admin")) {
			pw.println(name + "이 로그인 하셨습니다. 감사합니다.");
//			Cookie ck = new Cookie("name", name);
//			resp.addCookie(ck);		
			HttpSession session = req.getSession();
			session.setAttribute("name", name);
		} else {
			pw.println("로그인 정보를 다시 확인해주세요.");
			req.getRequestDispatcher("login.html").include(req, resp);
		}
		pw.close();
	}

}
