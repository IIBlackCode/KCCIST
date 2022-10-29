package QUIZE.Workshop.Java2ws1_Encapsulation.entity;

public class Ship {
	private String modelName;
	private int maxSpeed;
	private int numberLimit;
	private int replacement;
	public boolean available;
	
	public String getModelName() {
		return modelName;
	}
	
	


	public Ship(String modelName, int maxSpeed, int numberLimit, int replacement) {
		super();
		this.modelName = modelName;
		this.maxSpeed = maxSpeed;
		this.numberLimit = numberLimit;
		this.replacement = replacement;
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



	public int getReplacement() {
		return replacement;
	}



	public void setReplacement(int replacement) {
		this.replacement = replacement;
	}



	public boolean isAvailable() {
		return available;
	}



	public void setAvailable(boolean available) {
		this.available = available;
	}



	public void displayInfo() {
		System.out.println("-------------------------------------------");
		System.out.println(" 모 델 명 : " + modelName);
		System.out.println(" 최고속도 : " + maxSpeed + "km/h");
		System.out.println(" 최대정원 : " + numberLimit + "명");
		System.out.println(" 배 수 량 : " + replacement + "톤");
	}
}
