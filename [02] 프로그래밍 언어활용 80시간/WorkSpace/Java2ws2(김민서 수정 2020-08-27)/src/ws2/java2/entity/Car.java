package ws2.java2.entity;

public class Car extends Vehicle{
	private int mileage;
	
	public Car() {}
	
	public Car(String modelName, int maxSpeed, int numberLimit, int mileage) {
		//call the Parent Constructor :super(modelName, maxSpeed, numberLimit)
		super(modelName, maxSpeed, numberLimit);
		this.mileage = mileage;
	}

	public int getMileage() {
		return mileage;
	}

	public void setMileage(int mileage) {
		this.mileage = mileage;
	}
	
	@Override
	public void displayInfo() {
		//the Method of Parent Class : super.displayInfo();
		super.displayInfo();
		System.out.println(" Æò±Õ¿¬ºñ : " + mileage + "km/l");
	}

	@Override
	public String toString() {
		return "Car [mileage=" + mileage + ", modelName=" + modelName + ", maxSpeed=" + maxSpeed + ", numberLimit="
				+ numberLimit + ", available=" + available + ", getMileage()=" + getMileage() + ", getModelName()="
				+ getModelName() + ", getMaxSpeed()=" + getMaxSpeed() + ", getNumberLimit()=" + getNumberLimit()
				+ ", isAvailable()=" + isAvailable() + ", getClass()=" + getClass() + ", hashCode()=" + hashCode()
				+ ", toString()=" + super.toString() + "]";
	}
	
}
