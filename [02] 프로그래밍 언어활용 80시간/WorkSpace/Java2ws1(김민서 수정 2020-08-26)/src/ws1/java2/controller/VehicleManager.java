package ws1.java2.controller;

import ws1.java2.entity.*;

public class VehicleManager {
	Airplane[] airplaneArr;
	Car[] carArr;
	Ship[] shipArr;
	
	public VehicleManager() {
		airplaneArr = new Airplane[2];
		carArr = new Car[3];
		shipArr = new Ship[2];
		
		airplaneArr[0] = new Airplane("보잉747", 180, 5, 10);
		airplaneArr[1] = new Airplane("F-16",1600,1,1);
		carArr[0] = new Car("소나타3", 180, 5, 10);
		carArr[2] = new Car("스타렉스", 150, 10, 11);
		shipArr[0] = new Ship("크루즈2",30,400,35000);
		shipArr[1] = new Ship("노틸러스",25,150,15000);
	}
	
	public void displayVehicles(String title) {
		System.out.println(title);
		
		for (int inx = 0 ; inx < airplaneArr.length ; inx++) {
			airplaneArr[inx].displayInfo();
			airplaneArr[inx].available = true;
		}
		
		for (int inx = 0 ; inx < carArr.length ; inx++) {
			try {
				
//				if (!(carArr[inx] == null)) {
					carArr[inx].displayInfo();
					carArr[inx].available = true;
//				}
				
			} catch (NullPointerException e) {
				// TODO: handle exception
				System.out.println(inx+"번째 index에서 NullPointerException 발생 : "+e.getMessage());
			}
		}
		
		for (int inx = 0 ; inx < shipArr.length ; inx++) {
			shipArr[inx].displayInfo();
			shipArr[inx].available = true;
		}
		
		System.out.println();
	}
}

