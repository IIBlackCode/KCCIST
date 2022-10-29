package QUIZE.Workshop.Java2ws3.controller;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Iterator;

import QUIZE.Workshop.Java2ws3.entity.Airplane;
import QUIZE.Workshop.Java2ws3.entity.Car;
import QUIZE.Workshop.Java2ws3.entity.Ship;
import QUIZE.Workshop.Java2ws3.entity.Vehicle;


/*
 * 고정방식인 배열에서 다이나믹 확장구조를 사용하기 위해 ArrayList를 사용
 */
public class VehicleManager {
	//아래 코드는 배열을 참조하는 변수를 선언한 것이다.
	//ArrayList를 참조하도록 새로운 변수를 선언하시오.(변수명은  vehicleList)
	
	ArrayList<Vehicle> vehicleList = new ArrayList<Vehicle>();
	/*
	2. VehicleManager 클래스 내의 생성자(Constructor)를 완성한다.
		A. Vehicle 개체를 담을 수 있는 ArrayList 개체를 생성한다.
		B. Airplane, Car, Ship 개체들을 생성하면서 생성자를 이용해 값을	초기화하고 ArrayList 에 추가한다.
	*/
	public VehicleManager() {
		//아래 코드는 배열을 이용하도록 작성되었다.
		//ArrayList를 사용하도록 수정하시오.
		vehicleList.add(new Airplane("보잉747", 1300, 300, 4));
		vehicleList.add(new Airplane("F-16", 1600, 1, 1));
		vehicleList.add(new Car("소나타3", 180, 5, 10));
		vehicleList.add(new Car("티코", 130, 4, 15));
		vehicleList.add(new Car("스타렉스", 150, 10, 11));
		vehicleList.add(new Ship("크루즈2", 30, 400, 35000));
		vehicleList.add(new Ship("노틸러스", 25, 150, 15000));
		
	}
	
	public void displayVehicles(String title) {
		//아래 코드는 배열이 가리키는 모든 객체의 정보를 출력하도록 작성되었다.
		//ArrayList인 vehicleList에 담긴 모든 객체를 출력하도록 수정하시오.
		
		System.out.println(title);
		
		for (Vehicle v : vehicleList) {
			v.displayInfo();
		}
		
		System.out.println();
	}
	/*
	3. sortByModelName() 메서드를 작성한다.
		A. 전체적인 로직은 이전에 사용한 정렬 로직과 동일하다. 
		단지 개체 참조값을 얻어내거나 수정하는 방법이 배열(array)와 다를 뿐이다.
		B. ArrayList 의 메서드를 활용해서 개체의 modelName 을 기준으로 
		오름차순으로 정렬하도록 메서드의 기능을 완성한다.
	 */
	public void sortByModelName() {
		//아래 코드는 배열에 대해서 정렬을 수행하는 것이다.
		//ArrayList인 vehicleList에 대해서 정렬을 수행하는 코드로 변환하시오.
		
		/*
sort
public void sort(Comparator<? super E> c)

Description copied from interface: List

Sorts this list according to the order induced by the specified Comparator. 
All elements in this list must be mutually comparable using thespecified comparator (that is, c.compare(e1, e2) must not throwa ClassCastException for any elements e1 and e2in the list). 

If the specified comparator is null then all elements in thislist must implement the Comparable interface and the elements' natural ordering should be used. 

This list must be modifiable, but need not be resizable.
Specified by:sort in interface List<E>Parameters:c - the Comparator used to compare list elements.A null value indicates that the elements' natural ordering should be used

		 * 두 객체를 비교하기 위한 Comparator 사용
		 * 정렬대상 : vehicleList
		 * 비교기준 : Vehicle의 ModelName
		 */
		
		Collections.sort(vehicleList,new Comparator<Vehicle>() {

			@Override
			public int compare(Vehicle o1, Vehicle o2) {
				System.out.println("\t\t *** Soarting .... ***");
				System.out.println("\t\t o1 : "+o1.getModelName()+", o2 : "+o2.getModelName());
				
				/*
				if (o1.getModelName().compareTo(o2.getModelName()) > 0) {
					return 1;
				} else if (o1.getModelName().compareTo(o2.getModelName()) < 0){
					return -1;
				} else {
					return 0;
				}
				 */
				
				/*
				 * 성능향상을 위한 삼항연산자 사용
				 * o1.getModelName().compareTo(o2.getModelName()) < 0 : 오름차순
				 * o1.getModelName().compareTo(o2.getModelName()) > 0 : 내림차순
				 */
				return (o1.getModelName().compareTo(o2.getModelName()) < 0 ? -1 : (o1.getModelName() == o2.getModelName() ? 0 :1) );
			}
		});
		
	}

	/*
	4. displayVehicles1() 메서드를 작성한다.
		A. 새로운 for 문법을 이용하여 ArrayList 로부터 저장된 개체를 순차적으로 얻어낸다.
		B. 얻어낸 개체가 가지고 있는 displayInfo() 메서드를 호출한다.
	 */
	public void displayVehicles1(String title) {
		
		System.out.println(title);
		
		for (Vehicle v : vehicleList) {
			v.displayInfo();
		}
		System.out.println();
	}
	
	/*
	5. displayVehicles2() 메서드를 작성한다.
		A. ArrayList 로부터 Iterator 에 대한 참조값을 얻어내서 저장한다.
		B. while 안에서 iterator 를 이용해 순차적으로 저장된 개체에 대한 
		참조값을 얻어온 다음, 얻어낸 개체가 가지고 있는 displayInfo() 메서드를 호출한다.
	 */
	public void displayVehicles2(String title) {
		System.out.println(title);
		Iterator v = vehicleList.iterator();
		while (v.hasNext()) {
			Vehicle vv = (Vehicle)v.next();
			vv.displayInfo();
		}
		
	}
	
}

