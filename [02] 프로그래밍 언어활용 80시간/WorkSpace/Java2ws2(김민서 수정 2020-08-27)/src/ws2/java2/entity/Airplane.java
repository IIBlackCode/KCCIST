package ws2.java2.entity;

public class Airplane extends Vehicle{
	private int numOfEngine;
	
	public Airplane() {}
	
	public Airplane(String modelName, int maxSpeed, int numberLimit, int numOfEngine) {
		//call the Parent Constructor :super(modelName, maxSpeed, numberLimit);
		super(modelName, maxSpeed, numberLimit);
		this.numOfEngine = numOfEngine;
	}

	public int getNumOfEngine() {
		return numOfEngine;
	}

	public void setNumOfEngine(int numOfEngine) {
		this.numOfEngine = numOfEngine;
	}
	
	@Override
	public void displayInfo() {
		//the Method of Parent Class : super.displayInfo();
		super.displayInfo();
		System.out.println(" 엔진개수 : " + numOfEngine + "개");
	}

	@Override
	public String toString() {
		return "Airplane [numOfEngine=" + numOfEngine + ", modelName=" + modelName + ", maxSpeed=" + maxSpeed
				+ ", numberLimit=" + numberLimit + ", available=" + available + ", getNumOfEngine()=" + getNumOfEngine()
				+ ", getModelName()=" + getModelName() + ", getMaxSpeed()=" + getMaxSpeed() + ", getNumberLimit()="
				+ getNumberLimit() + ", isAvailable()=" + isAvailable() + ", getClass()=" + getClass() + ", hashCode()="
				+ hashCode() + ", toString()=" + super.toString() + "]";
	}
	
	
}
