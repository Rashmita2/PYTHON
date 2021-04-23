
public class TwoD {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[][] cars = new String[3][3];
		cars[0][0] = "Camro";
		cars[0][1] = "Toyota";
		cars[0][1] = "Corolla";
		cars[1][0] = "Nissan";
		cars[1][1] = "Tesla";
		cars[1][2] = "Tesla";
		cars[2][0] = "Tesla";
		cars[2][1] = "Tesla";
		cars[2][2] = "Tesla";
		
		for(int i=0; i<cars.length; i++) {
			System.out.println();
			for(int j=0; j<cars[i].length; j++) {
				System.out.print(cars[i][j]+ " ");
				
			}
		}
		
	}

}
