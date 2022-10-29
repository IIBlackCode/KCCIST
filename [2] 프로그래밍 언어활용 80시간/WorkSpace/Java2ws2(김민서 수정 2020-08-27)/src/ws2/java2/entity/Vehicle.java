package ws2.java2.entity;

public class Vehicle {
	
	//공통변수
	String modelName;
	int maxSpeed;
	int numberLimit;
	boolean available;
	
	//Default Constructor
	public Vehicle() {
		// TODO Auto-generated constructor stub
	}
	
	//다른 패키지에서 접근하기 위한 public 접근제어자 설정
	public Vehicle(String modelName, int maxSpeed, int numberLimit) {
		this.modelName = modelName;
		this.maxSpeed = maxSpeed;
		this.numberLimit = numberLimit;
	}
	
	//상속받기 위한 displayInfo method
	public void displayInfo() {
		
		System.out.println("-------------------------------------------");
		System.out.println(" 모 델 명 : " + modelName);
		System.out.println(" 최고속도 : " + maxSpeed + "km/h");
		System.out.println(" 최대정원 : " + numberLimit + "명");
	}
	
	//공통변수에 대한 getter, setter
	public String getModelName() {
		return modelName;
	}
	public void setModelName(String modelName) {
		this.modelName = modelName;
	}
	public int getMaxSpeed() {
		return maxSpeed;
	}
	public void setMaxSpeed(int maxSpeed) {
		this.maxSpeed = maxSpeed;
	}
	public int getNumberLimit() {
		return numberLimit;
	}
	public void setNumberLimit(int numberLimit) {
		this.numberLimit = numberLimit;
	}
	public boolean isAvailable() {
		return available;
	}
	public void setAvailable(boolean available) {
		this.available = available;
	}
	
}
