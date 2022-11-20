<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>자재 추가</title>
</head>
<body>
	<form action="PoItemAddProcess.jsp" method="post">
	<a href="PoItemList.jsp">자재목록</a>
	<table border="1" cellspacing="0" cellpadding="2">
	<tr>
		<td>자재번호</td><td><input type="text" name="ITEM_NO"></td>
	</tr>
	<tr>
		<td>자재명</td><td><input type="text" name="ITEM_NAME"></td>
	</tr>
	<tr>
		<td>단가</td><td><input type="text" name="UNIT_PRICE"></td>
	</tr>
	<tr>
		<td>단위</td><td><input type="text" name="ITEM_UNIT"></td>
	</tr>
	<tr>
		<td colspan="2">
		<input type="submit" value="추가">
		<input type="reset" value="취소">
		</td>
	</tr>
	</table>
	</form>
</body>
</html>