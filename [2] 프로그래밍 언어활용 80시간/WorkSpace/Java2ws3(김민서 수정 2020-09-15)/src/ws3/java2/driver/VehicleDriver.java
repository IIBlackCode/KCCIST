package ws3.java2.driver;

import ws3.java2.controller.*;

public class VehicleDriver {
	public static void main(String[] args) {
		VehicleManager vm = new VehicleManager();
		vm.displayVehicles(">> 재고 목록 <<");
		vm.sortByModelName();
		vm.displayVehicles(">> 모델명으로 정렬된 재고 목록 <<");
		vm.displayVehicles1(">> 새로운 for 문법 <<");
		vm.displayVehicles2(">> displayVehicles2() <<");
	}
}
