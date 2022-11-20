package QUIZE.Workshop.Java2ws3.entity;

public class Airplane extends Vehicle {
	private int numOfEngine;
	
	public Airplane(String modelName, int maxSpeed, int numberLimit, int numOfEngine) {
		super(modelName, maxSpeed, numberLimit);
		this.numOfEngine = numOfEngine;
	}
	
	public int getNumOfEngine() {
		return numOfEngine;
	}

	public void setNumOfEngine(int numOfEngine) {
		this.numOfEngine = numOfEngine;
	}

	public void displayInfo() {
		super.displayInfo();
		System.out.println(" 엔진개수 : " + numOfEngine + "개");
	}

}
