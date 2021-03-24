import java.util.*;

public class Except {

    public static void main(String[] args) {
        try {
            int[] numbers = { 3, 4, 5, 2 };
            System.out.println(numbers[10]);
        } catch (Exception e) {
            System.out.println("Not working");
        } finally {
            System.out.println("The try catch block is executed");
        }
    }
}
