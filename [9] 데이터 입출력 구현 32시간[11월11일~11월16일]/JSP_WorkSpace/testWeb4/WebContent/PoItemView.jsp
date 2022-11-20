<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="com.mycompany.bo.*" %>
<%@ page import="com.mycompany.dao.*" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	String itemNo = request.getParameter("ITEM_NO");
	PoItemBo ib = PoItemDao.getPoItemByNo(itemNo);
%>
<table border="1" cellspacing="0" cellpadding="2">
<tr>
	<td>자재번호</td><td><%=ib.getItemNo()%></td>
</tr>
<tr>
	<td>자재명</td><td><%=ib.getItemName()%></td>
</tr>
<tr>
	<td>단가</td><td><%=ib.getUnitPrice()%></td>
</tr>
<tr>
	<td>단위</td><td><%=ib.getItemUnit()%></td>
</tr>
</table>
<a href="PoItemUpdate.jsp?ITEM_NO=<%=itemNo%>">수정</a>
<a href="PoItemDeleteProcess.jsp?ITEM_NO=<%=itemNo%>">삭제</a>
</body>
</html>


