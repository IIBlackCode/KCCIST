<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="com.mycompany.Student" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	//com.mycompany.Student s = new com.mycompany.Student();
	Student s = new Student();
	s.setName("John");
	s.setAge(20);
	out.println(s.getName() + ", " + s.getAge());
%>
<jsp:useBean id="s2" class="com.mycompany.Student"></jsp:useBean>
<%
	s2.setName("jane");
	out.println(s2.getName());
%>
<jsp:setProperty property="name" name="s2" value="Tom"/>
<jsp:getProperty property="name" name="s2"/>
<br>
<jsp:useBean id="s3" class="com.mycompany.Student"></jsp:useBean>
<jsp:setProperty property="name" name="s3" value="John2"/>
<jsp:getProperty property="name" name="s3"/>


</body>
</html>