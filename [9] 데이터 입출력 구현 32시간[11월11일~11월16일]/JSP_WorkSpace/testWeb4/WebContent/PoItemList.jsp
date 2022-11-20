<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="com.mycompany.bo.*" %>
<%@ page import="com.mycompany.dao.*" %>
<%@ page import="java.util.*" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>자재 목록</title>
</head>
<body>
<%
	List<PoItemBo> list = PoItemDao.getPoItems();
%>
<a href="PoItemAdd.jsp">자재추가</a>
<table border="1" cellspacing="0" cellpadding="2">
<tr>
	<td>자재순번</td><td>자재명</td><td>단가</td><td>단위</td>
</tr>
<% for(PoItemBo i : list) { %>
<tr>
	<td><%=i.getItemNo()%></td>
	<td><a href='PoItemView.jsp?ITEM_NO=<%=i.getItemNo()%>'><%=i.getItemName()%></a></td>
	<td><%=i.getUnitPrice()%></td>
	<td><%=i.getItemUnit()%></td>
</tr>
<% } %>
</table>

</body>
</html>




