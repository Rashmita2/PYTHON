
import java.io.File;
import java.util.Scanner;

public class Reading {
	public static void main(String[] args) throws Exception {
		File file = new File("./mytext.txt");
		Scanner in = new Scanner(file);
		while (in.hasNextLine())
			System.out.println(in.nextLine());
	}
}
