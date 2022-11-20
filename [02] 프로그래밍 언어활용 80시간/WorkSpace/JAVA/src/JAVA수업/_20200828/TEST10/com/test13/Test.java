package JAVA¼ö¾÷._20200828.TEST10.com.test13;

interface WriteLog {
	void write();
}

class FileLog implements WriteLog {

	@Override
	public void write() {
		System.out.println("File Log");
	}
	
}

class DatabaseLog implements WriteLog {

	@Override
	public void write() {
		System.out.println("DataBase Log");
	}
}

class WriteManager {
	WriteLog w;
	public WriteManager(WriteLog w) {
		this.w = w;
	}
	
	public void execute() {
		w.write();
	}
}

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		WriteManager o = new WriteManager(new FileLog());
		o.execute();
		WriteManager o2 = new WriteManager(new DatabaseLog());
		o2.execute();
	}

}
