package com.test4;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/LoginServlet")
public class LoginServlet extends HttpServlet {
	public void doPost(HttpServletRequest req,
			HttpServletResponse res) throws IOException {
		res.setContentType("text/html;charset=UTF-8");
		PrintWriter pw = res.getWriter();
		String userName = req.getParameter("userName");
		String userPwd = req.getParameter("userPwd");
		if(userName.equals("test")) {
			pw.println("로그인 하셨습니다.");
		} else  {
			pw.println("다시 확인해주세요.");
		}
		pw.close();
	}
}
