<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="com.mycompany.bo.*" %>
<%@ page import="com.mycompany.dao.*" %>
<%
	String itemNo = request.getParameter("ITEM_NO");
	int ret = PoItemDao.delete(itemNo);
	response.sendRedirect("PoItemList.jsp");
%>