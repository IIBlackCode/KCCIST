package ws1.java2.entity;

public class Airplane {
	private String modelName;
	private int maxSpeed;
	private int numberLimit;
	private int numOfEngine;
	public boolean available;
	
	public Airplane(String modelName, int maxSpeed, int numberLimit, int numOfEngine) {
		super();
		this.modelName = modelName;
		this.maxSpeed = maxSpeed;
		this.numberLimit = numberLimit;
		this.numOfEngine = numOfEngine;
	}



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



	public int getNumOfEngine() {
		return numOfEngine;
	}



	public void setNumOfEngine(int numOfEngine) {
		this.numOfEngine = numOfEngine;
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
		System.out.println(" 엔진개수 : " + numOfEngine + "개");
	}
}
