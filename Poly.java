class Animal {
    public void Sound() {
        System.out.println("Sound of dog is bow woo");
    }
}

class Truck extends Animal {
    public void Sound() {
        System.out.println("Sound of Truck is peep peep");
    }
}

public class Poly {
    public static void main(String[] args) {
        Animal myDog = new Animal();
        myDog.Sound();
        Truck myTruck = new Truck();
        myTruck.Sound();
    }
}
