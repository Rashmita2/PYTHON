import java.util.*;
public class LetsDoEnum {
	
enum Levels {
	HIGH,
	MEDIUM,
	LOW
}

public static void main(String [] args) {
	//iterating through enums
	for (Levels l : Levels.values()) { 
	    System.out.println(l); 
	}
	
}
}
