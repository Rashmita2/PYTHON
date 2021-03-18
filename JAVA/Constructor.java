public class Constructor {
    int modelYear;
    String modelName;

    //Creating a constructor
    public Constructor(int year, String name) {
        modelYear = year;
        modelName = name;
    }
    public static void main(String[] args) {
        Constructor myCar = new Constructor(2011, "Audi");
        System.out.println(myCar.modelName + " " + myCar.modelYear);
    }
}
