import java.util.*;
public class Nested {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int rows;
		int cols;
		String symbol = "";
		System.out.println("Enter number of rows: ");
		rows = in.nextInt();
		System.out.println("Enter number of columns: ");
		cols = in.nextInt();
		System.out.println("Enter symbol to use: ");
		symbol = in.next();
		for(int i=1; i<=rows; i++) {
			System.out.println();
			for(int j= 1; j<=cols; j++) {
				System.out.print(symbol);
			}
		}
	}
}
