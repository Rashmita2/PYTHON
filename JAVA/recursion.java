public class recursion {
    public static void main(String[] args) {
        int result = sum(5);
        System.out.println(result);
    }

    public static int sum(int j) {
        if (j > 0) {
            return j + sum(j - 1);
        } else {
            return 0;
        }
    }
}
