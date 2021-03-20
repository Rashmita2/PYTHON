import java.util.Scanner;

public class myClass {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("What is your name?");
        String username = in.nextLine();
        System.out.println("Username is:" + username);
    }
}
