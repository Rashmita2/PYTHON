public class QRunner {
    public static void main(String[] args) {
        Queue q = new Queue();
        q.enqueue(5);
        q.enqueue(86);
        q.enqueue(6);

        q.dequeue();

        q.show();
    }
}
