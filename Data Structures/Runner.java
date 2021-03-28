import java.util.*;

public class Runner {
    public static void main(String[] args) {
        link list = new link();
        list.insert(5);
        list.insert(45);
        list.insertAtStart(34);
        list.insertAt(1, 55);
        list.deleteAt(2);
        list.show();

    }
}
