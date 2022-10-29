package QUIZE.Workshop.Java2ws2_InheritanceAndPolymorphism.driver;

import QUIZE.Workshop.Java2ws2_InheritanceAndPolymorphism.controller.VehicleManager;

//import ws2.java2.controller.*;

public class VehicleDriver {
	public static void main(String[] args) {
		VehicleManager vm = new VehicleManager();
		vm.displayVehicles(">> 재고 목록 <<");
		vm.sortByModelName();
		vm.displayVehicles(">> 모델명으로 정렬된 재고 목록 <<");
	}
}