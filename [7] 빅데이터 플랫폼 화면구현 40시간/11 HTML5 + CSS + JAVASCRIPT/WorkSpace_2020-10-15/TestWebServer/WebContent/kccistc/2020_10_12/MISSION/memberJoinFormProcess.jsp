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
		String userName = request.getParameter("userName");
		String userId= request.getParameter("userId");
		String userPw= request.getParameter("userPw");
		String userPwCheck= request.getParameter("userPwCheck");
		String userEmail= request.getParameter("userEmail");
		String gender= request.getParameter("gender");
		String userTel= request.getParameter("userTel");
		String userBirth= request.getParameter("userBirth");
		String userColor= request.getParameter("userColor");
		String interests= request.getParameter("interests");
		
		out.println(userName);
		out.println(userId);
		out.println(userPw);
		out.println(userPwCheck);
		out.println(userEmail);
		out.println(gender);
		out.println(userTel);
		out.println(userBirth);
		out.println(userColor);
		out.println(interests);		
		
	%>
	<script>
		if gender == male{
			<%=gender%> = "남자";
		}
		if gender == female{
			<%=gender%> = "여자";
		}
		if gender == other{
			<%=gender%> = "그외";
		}
	</script>
	
	<form method="get" action="memberJoinFormProcess.jsp">
		<!-- <table border = 1> -->
		<table>
			<tr>	
				<h1>회원가입 완료</h1>
			</tr>
			<tr>
				<td>이름 :</td>
				<td colspan="3"><%=userName %></td>
			</tr>
			<tr>
				<td>ID :</td>
				<td><%=userId %></td>
			</tr>
			<tr>
				<td>PW :</td>
				<td><%=userPw %></td>
			</tr>
			<tr>
				<td>PW확인 :</td>
				<td><%=userPwCheck %></td>
			</tr>
			<tr>
				<td>이메일 :</td>
				<td><%=userEmail %></td>
			</tr>
			<tr>
				<td>성별 :</td>
				<td>
					<%=gender %>
				</td>
				
			</tr>
			<tr>
				<td>전화번호 :</td>
				<td><%=userTel %></td>
			</tr>
			<tr>
				<td>생일 :</td>
				<td><%=userBirth %></td>
			</tr>
			<tr>
				<td>좋아하는 색깔 :</td>
				<td><input type="color" name="userColor" size="20" value="<%=userColor%>"></td>
			</tr>
			<tr>
				<td>관심분야 :</td>
				<td>
					<%=interests %>
				</td>
			</tr>
			
			
			<tr>
				<td align="center">
					<input type="submit" value="로그인">
					<input type="button" value="취소">
				</td>
			</tr>
			
		</table>
	</form>
	
</body>
</html>