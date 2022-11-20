<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<jsp:useBean id="s1" class="com.mycompany.Student"></jsp:useBean>
<jsp:setProperty property="*" name="s1"/>
<br>
<jsp:getProperty property="name" name="s1"/><br>
<jsp:getProperty property="age" name="s1"/>
</body>
</html>