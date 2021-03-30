import java.util.*;

public class Threading extends Thread {
    public static void main(String[] args) {
        Threading t1 = new Threading();
        t1.start();
        System.out.println("This code is outside of the thread");
    }

    public void run() {
        System.out.println("This code is running in a thread");
    }
}
