package ws2.java2.entity;

public class Ship extends Vehicle{
	private int replacement;
	
	public Ship() {}
	
	public Ship(String modelName, int maxSpeed, int numberLimit, int replacement) {
		//call the Parent Constructor :super(modelName, maxSpeed, numberLimit);
		super(modelName, maxSpeed, numberLimit);
		this.replacement = replacement;
	}
	
	public int getReplacement() {
		return replacement;
	}

	public void setReplacement(int replacement) {
		this.replacement = replacement;
	}
	
	@Override
	public void displayInfo() {
		//the Method of Parent Class : super.displayInfo();
		super.displayInfo();
		System.out.println(" ¹è ¼ö ·® : " + replacement + "Åæ");
	}

	@Override
	public String toString() {
		return "Ship [replacement=" + replacement + ", modelName=" + modelName + ", maxSpeed=" + maxSpeed
				+ ", numberLimit=" + numberLimit + ", available=" + available + ", getReplacement()=" + getReplacement()
				+ ", getModelName()=" + getModelName() + ", getMaxSpeed()=" + getMaxSpeed() + ", getNumberLimit()="
				+ getNumberLimit() + ", isAvailable()=" + isAvailable() + ", getClass()=" + getClass() + ", hashCode()="
				+ hashCode() + ", toString()=" + super.toString() + "]";
	}
	
}
