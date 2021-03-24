public class diff {
    // Static method
    static void myStatic() {
        System.out.println("This is static method");
    }

    // Public method
    public void myPublic() {
        System.out.println("This is main method");
    }

    // Main method
    public static void main(String[] args) {
        // static doesn't need to create the object
        myStatic();
        // myPublic(); //runs into an error
        // public need object
        diff myobj = new diff();
        myobj.myPublic();

    }
}
