<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="com.mycompany.bo.*" %>
<%@ page import="com.mycompany.dao.*" %>
<%
	String itemNo = request.getParameter("ITEM_NO");
	String itemName = request.getParameter("ITEM_NAME");
	int unitPrice = Integer.parseInt(request.getParameter("UNIT_PRICE"));
	String itemUnit = request.getParameter("ITEM_UNIT");

	PoItemBo ib = new PoItemBo();
	ib.setItemNo(itemNo);
	ib.setItemName(itemName);
	ib.setUnitPrice(unitPrice);
	ib.setItemUnit(itemUnit);
	PoItemDao.update(ib);
	//out.println("PoItem 추가 완료");
	//out.println(itemNo + ", " + itemName + ", " 
	//	+ unitPrice + "," + itemUnit);	
	response.sendRedirect("PoItemList.jsp");
%>