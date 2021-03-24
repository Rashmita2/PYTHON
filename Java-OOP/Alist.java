import java.util.ArrayList;
import java.util.Collections;

public class Alist {

    public static void main(String[] args) {

        // create an arraylist
        ArrayList<String> Flowers = new ArrayList<String>();
        Flowers.add("Rose");
        Flowers.add("lily");
        Flowers.add("lotus");
        // modify the elements
        Flowers.set(0, "Pancy");
        Collections.sort(Flowers);
        System.out.println(Flowers);
        System.out.println(Flowers.get(2));

    }

}
