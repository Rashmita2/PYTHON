public class Inherit {
    protected int year = 2021;

    public void info() {
        System.out.println("This is the info.");
    }
}

class Car extends Inherit {
    private String model = "Volvo";

    public static void main(String[] args) {
        Car myCar = new Car();
        myCar.info();
        System.out.println(myCar.year + " " + myCar.model);
    }
}
