package Chapter._18._2;

import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class IOExceptionCase03 {

	public static void main(String[] args) {

		try {
			md1();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private static void md1() throws IOException {
		md2();
	}

	private static void md2() throws IOException{
		Path file = Paths.get("c:\\javastudy\\Simple.txt");
		BufferedWriter writer = null;
		writer = Files.newBufferedWriter(file);	//IOException 발생 가능
		writer.write('A');						//IOException 발생 가능
		writer.write('B');		
		
		if (writer != null) {
			writer.close();						//IOException 발생 가능
		}
	}

}
