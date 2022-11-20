package Chapter._18._2;

import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class IOExceptionCase02 {

	public static void main(String[] args) {

		Path file = Paths.get("c:\\javastudy\\Simple.txt");
		BufferedWriter writer = null;
//		writer = Files.newBufferedWriter(file);	//IOException 발생 가능
//		writer.write('A');						//IOException 발생 가능
//		writer.write('B');						//IOException 발생 가능

		if (writer != null) {
//			writer.close();						//IOException 발생 가능
		}
	}

}
