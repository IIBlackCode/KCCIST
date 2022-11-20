<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="com.mycompany.bo.*" %>
<%@ page import="com.mycompany.dao.*" %>
<%
	String itemNo = request.getParameter("ITEM_NO");
	PoItemBo ib = PoItemDao.getPoItemByNo(itemNo);
%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>자재 수정</title>
</head>
<body>
	<form action="PoItemUpdateProcess.jsp" method="post">
	<a href="PoItemList.jsp">자재목록</a>
	<table border="1" cellspacing="0" cellpadding="2">
	<tr>
		<td>자재번호</td><td><%=itemNo%>
		<input type="hidden" name="ITEM_NO" value=<%=itemNo%>>
		</td>
	</tr>
	<tr>
		<td>자재명</td><td><input type="text" name="ITEM_NAME" value=<%=ib.getItemName()%>></td>
	</tr>
	<tr>
		<td>단가</td><td><input type="text" name="UNIT_PRICE" value=<%=ib.getUnitPrice()%>></td>
	</tr>
	<tr>
		<td>단위</td><td><input type="text" name="ITEM_UNIT" value=<%=ib.getItemUnit()%>></td>
	</tr>
	<tr>
		<td colspan="2">
		<input type="submit" value="수정">
		<input type="reset" value="취소">
		</td>
	</tr>
	</table>
	</form>
</body>
</html>