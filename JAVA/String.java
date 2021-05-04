import java.util.*;
public class pen {
public static void main(String[] args) {
	String text1 = "hello";
	String text2 = "hello";
	if(text1 == text2) {
		System.out.println("String1 == string2");
	}else {
		System.out.println("String1 != string2");
	}
	
	String s1 = new String("hello");
	String s2 = new String("hello");
	
	if(s1 == s2) {
		System.out.println("String1 == string2");
	}else {
		System.out.println("String1 != string2");
	}
	
	if(s1.equals(s1)) {
		System.out.println("String1 == string2");
	}else {
		System.out.println("String1 != string2");
	}
	if(s1.compareTo(s2) == 0) {
		System.out.println("s1 is compared to s2");
	}
	else {
		System.out.println("s1 is not compared to s2");
	}
}
}

