public class StackRun {
    public static void main(String[] args) {
        Stack nums = new Stack();
        nums.push(23);
        nums.push(6);
        nums.push(34);
        System.out.println(nums.peek());
        System.out.println(nums.pop());
        nums.show();
    }
}
