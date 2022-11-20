package com.mycompany.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import com.mycompany.bo.PoItemBo;
// save, update, delete, list(여러건), view(한건)
// PO_ITEM (ITEM_NO, ITEM_NAME, UNIT_PRICE, ITEM_UNIT)
public class PoItemDao {	
	public static Connection getConnection() {
		Connection conn = null;
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			conn = DriverManager.getConnection("jdbc:oracle:thin:@10.10.14.125:1521:company","scott","1234");
		} catch (ClassNotFoundException | SQLException e) {
			e.printStackTrace();
		}
		return conn;
	}
	// INSERT INTO PO_ITEM VALUES(?, ?, ?, ?)
	public static int save(PoItemBo poItem) { 		
		int status = 0;
		Connection conn = getConnection();
		try {
			String strSql = "INSERT INTO PO_ITEM VALUES(?, ?, ?, ?)";
			PreparedStatement ps;
			ps = conn.prepareStatement(strSql);
			ps.setString(1, poItem.getItemNo());
			ps.setString(2, poItem.getItemName());
			ps.setInt(3, poItem.getUnitPrice());
			ps.setString(4, poItem.getItemUnit());
			status = ps.executeUpdate();
		} catch (SQLException e) {
			e.printStackTrace();
		} 
		return status;
	}
	// UPDATE PO_ITEM SET ?, ?, ? WHERE ?
	public static int update(PoItemBo poItem) { 
		int status = 0;
		Connection conn = getConnection();
		try {
			String strSql = "UPDATE PO_ITEM SET ITEM_NAME = ?, UNIT_PRICE = ?, ITEM_UNIT = ? WHERE RTRIM(ITEM_NO) = ?";
			PreparedStatement ps;
			ps = conn.prepareStatement(strSql);			
			ps.setString(1, poItem.getItemName());
			ps.setInt(2, poItem.getUnitPrice());
			ps.setString(3, poItem.getItemUnit());
			ps.setString(4, poItem.getItemNo());
			status = ps.executeUpdate();
		} catch (SQLException e) {
			e.printStackTrace();
		} 
		return status;
	}
	// DELETE PO_ITEM WHERE ?
	public static int delete(String itemNo) { 
		int status = 0;
		Connection conn = getConnection();
		try {
			String strSql = "DELETE FROM PO_ITEM WHERE RTRIM(ITEM_NO) = ?";
			PreparedStatement ps;
			ps = conn.prepareStatement(strSql);
			ps.setString(1, itemNo);
			status = ps.executeUpdate();
		} catch (SQLException e) {
			e.printStackTrace();
		} 
		return status; 
	}
	// SELECT * FROM PO_ITEM
	public static List<PoItemBo> getPoItems() { 
		List<PoItemBo> list = new ArrayList<PoItemBo>();
		Connection conn = getConnection();
		String strSql = "SELECT * FROM PO_ITEM ORDER BY ITEM_NO DESC";
		try {
			PreparedStatement ps = conn.prepareStatement(strSql);
			ResultSet rs = ps.executeQuery();
			while(rs.next()){
				PoItemBo ib = new PoItemBo();
				ib.setItemNo(rs.getString("ITEM_NO"));
				ib.setItemName(rs.getString("ITEM_NAME"));
				ib.setUnitPrice(rs.getInt("UNIT_PRICE"));
				ib.setItemUnit(rs.getString("ITEM_UNIT"));
				list.add(ib);
			}
			
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
		return list;
		
	}
	// SELECT * FROM PO_ITEM WHERE ?
	public static PoItemBo getPoItemByNo(String itemNo) { 
		Connection conn = getConnection();
		String strSql = "SELECT * FROM PO_ITEM WHERE RTRIM(ITEM_NO) = ?";
		PoItemBo ib = new PoItemBo();
		try {
			PreparedStatement ps = conn.prepareStatement(strSql);
			ps.setString(1, itemNo.trim());
			ResultSet rs = ps.executeQuery();
			if(rs.next()){
				ib.setItemNo(rs.getString("ITEM_NO"));
				ib.setItemName(rs.getString("ITEM_NAME"));
				ib.setUnitPrice(rs.getInt("UNIT_PRICE"));
				ib.setItemUnit(rs.getString("ITEM_UNIT"));
			}			
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
		return ib;
	
	}
}
