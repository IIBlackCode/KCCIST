package ws2.java2.controller;

import ws2.java2.entity.*;

public class VehicleManager_원본유지 {
	Airplane[] airplaneArr;
	Car[] carArr;
	Ship[] shipArr;

	static Vehicle[][] vehicleArr;

	public VehicleManager_원본유지() {
		airplaneArr = new Airplane[2];
		carArr = new Car[3];
		shipArr = new Ship[2];

		airplaneArr[0] = new Airplane("보잉747", 1300, 300, 4);
		airplaneArr[1] = new Airplane("F-16", 1600, 1, 1);

		carArr[0] = new Car("소나타3", 180, 5, 10);
		carArr[1] = new Car("티코", 130, 4, 15);
		carArr[2] = new Car("스타렉스", 150, 10, 11);

		shipArr[0] = new Ship("크루즈2", 30, 400, 35000);
		shipArr[1] = new Ship("노틸러스", 25, 150, 15000);
	}

	public void displayVehicles(String title) {
		System.out.println(title);

		for (int inx = 0; inx < airplaneArr.length; inx++) {
			airplaneArr[inx].displayInfo();
			airplaneArr[inx].setAvailable(true);
		}

		for (int inx = 0; inx < carArr.length; inx++) {
			carArr[inx].displayInfo();
			carArr[inx].setAvailable(true);
		}

		for (int inx = 0; inx < shipArr.length; inx++) {
			shipArr[inx].displayInfo();
			shipArr[inx].setAvailable(true);
		}

		System.out.println();
	}

	public void sortByModelName() {

		/*
		 * 추가한 메서드 내에서 
		 * 배열에 대한 참조변수(vehicleArr)를 이용하여 
		 * 배열 내의 개체들에 대해서 
		 * 모델명(modelName)의 오름차순으로 정렬을 수행하도록 
		 * 이중 for 문을 사용해 코드를 작성한다
		 */
		
		System.out.println("*********** [1]. vehicleArr에 대입");
		vehicleArr = new Vehicle[3][3];
		for (int i = 0; i < vehicleArr.length; i++) {
			for (int j = 0; j < vehicleArr.length; j++) {
				try {
					if (i == 0) {
						vehicleArr[0][j] = airplaneArr[j];
						System.out.println("[" + i + "][" + j + "]"+vehicleArr[0][j].getModelName());
					} else if (i == 1) {
						vehicleArr[1][j] = carArr[j];
						System.out.println("[" + i + "][" + j + "]"+vehicleArr[1][j].getModelName());
					} else if (i == 2) {
						vehicleArr[2][j] = shipArr[j];
						System.out.println("[" + i + "][" + j + "]"+vehicleArr[2][j].getModelName());
					}
				} catch (ArrayIndexOutOfBoundsException e) {
//					System.out.println("[" + i + "][" + j + "]에서 null 발생");
					// TODO: handle exception
				}//the end of try ~ catch
			}//the end of for j
		}//the end of for i
		
		System.out.println("*********** [2]. 대입 결과 출력");
		for (int i = 0; i < vehicleArr.length; i++) {
			for (int j = 0; j < vehicleArr.length; j++) {
				try {
					System.out.println("[" + i + "][" + j + "]"+vehicleArr[i][j].getModelName()+"\t" + (int)(vehicleArr[i][j].getModelName()).charAt(0));
//						System.out.println(vehicleArr[i][j].toString());
				} catch (NullPointerException e) {
//					System.out.println("[" + i + "][" + j + "]에서 null 발생");
					// TODO: handle exception
				}//the end of try ~ catch
			}//the end of for j
		}//the end of for i
		
		System.out.println("*********** [3]. 순서 정렬");
		System.out.println("i = 0");
		for (int i = 0; i < vehicleArr.length-1; i++) {
			boolean changed = false;
			for (int j = 0; j < vehicleArr.length-1-i; j++) {
				try {
					
//					System.out.println("[" + i + "][" + j + "]" + (int)(vehicleArr[i][j].getModelName()).charAt(0));
					if (((int)(vehicleArr[0][j].getModelName()).charAt(0)>(int)((vehicleArr[0][j+1].getModelName()).charAt(0))) && (vehicleArr[1][j] != null)) {
						Vehicle temp = vehicleArr[0][j];
						vehicleArr[0][j] = vehicleArr[0][j+1];
						vehicleArr[0][j+1] = temp;
						changed = true;
//						System.out.println("[" + i + "][" + j + "]자리바꿈!");
					}
					if (! changed) break; 
					
				} catch (NullPointerException e) {
//					System.out.println("[" + i + "][" + j + "]에서 null 발생");
					// TODO: handle exception
				}//the end of try catch
			}// the end of for j
		}//the end of for i
		
		System.out.println("i = 1");
		for (int i = 0; i < 3-1; i++) {
			boolean changed = false;
			for (int j = 0; j < 3; j++) {
				try {
					
//					System.out.println("[" + i + "][" + j + "]" + (int)(vehicleArr[1][j].getModelName()).charAt(0));
//					System.out.println("[" + i + "][" + (j+1) + "]" + (int)(vehicleArr[1][j+1].getModelName()).charAt(0));
					if ((int)(vehicleArr[1][j].getModelName()).charAt(0)>(int)((vehicleArr[1][j+1].getModelName()).charAt(0))) {
						Vehicle temp = vehicleArr[1][j];
						vehicleArr[1][j] = vehicleArr[1][j+1];
						vehicleArr[1][j+1] = temp;
//						changed = true;
//						System.out.println("[" + i + "][" + j + "]자리바꿈!");
					}
//					if (! changed) break; 
					
				} catch (NullPointerException|ArrayIndexOutOfBoundsException e) {
//					System.out.println("[" + i + "][" + j + "]에서 null 발생");
					// TODO: handle exception
				}//the end of try ~ catch
			}// the end of for j
		}//the end of for i
		
		System.out.println("i = 2");
		for (int i = 0; i < 3-1; i++) {
			boolean changed = false;
			for (int j = 0; j < 3-1; j++) {
				try {
					
					if (((int)(vehicleArr[2][j].getModelName()).charAt(0)>(int)((vehicleArr[2][j+1].getModelName()).charAt(0))) && (vehicleArr[2][j] != null)) {
						Vehicle temp = vehicleArr[2][j];
						vehicleArr[2][j] = vehicleArr[2][j+1];
						vehicleArr[2][j+1] = temp;
						changed = true;
//						System.out.println("[" + i + "][" + j + "]자리바꿈!");
					}
					if (! changed) break; 
					
				} catch (NullPointerException e) {
//					System.out.println("[" + i + "][" + j + "]에서 null 발생");
				}//the end of try ~ catch
			}//the end of for j
		}//the end of for i
		
		System.out.println("*********** [4]. 결과 출력");
		for (int i = 0; i < vehicleArr.length; i++) {
			for (int j = 0; j < vehicleArr.length; j++) {
				try {
//					System.out.println("[" + i + "][" + j + "]" + (int)(vehicleArr[i][j].getModelName()).charAt(0));
					System.out.println("[" + i + "][" + j + "]" + (vehicleArr[i][j].getModelName()));
//						System.out.println(vehicleArr[i][j].toString());
				} catch (NullPointerException e) {
//					System.out.println("[" + i + "][" + j + "]에서 null 발생");
					// TODO: handle exception
				}//the end of try ~ catcy
			}//the end of for j
		}//the end of for i
		
	}// the end of method sortByModelName
	
}//the end of class
