//MultiThreading in Java
class Greeting extends Thread {
    public void run() {
        System.out.println("Hello");
        try {
            Thread.sleep(1000);
        } catch (Exception e) {
        }
    }
}

class Driver extends Thread {
    public void run() {
        System.out.println("Hi");
    }
}

public class ThreadDemo {
    public static void main(String[] args) {
        Greeting obj1 = new Greeting();
        Driver obj2 = new Driver();
        obj1.start();
        obj2.start();// starts call the run method

    }
}
