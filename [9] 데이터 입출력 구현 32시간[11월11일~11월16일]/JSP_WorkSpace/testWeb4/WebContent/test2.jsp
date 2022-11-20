<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
	<%
		//response.sendRedirect("http://www.naver.com");
		String test2Value = config.getInitParameter("test2Value");
		out.println(test2Value);
		String test3Value = application.getInitParameter("test3Value");
		out.println(test3Value);
		//application.setAttribute(arg0, arg1)
		//session.setAttribute(arg0, arg1)
	%>
</body>
</html>