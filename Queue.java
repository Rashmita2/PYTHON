public class Queue {
    int queue[] = new int[5];
    int size, front, rear;

    // add to the queue
    public void enqueue(int data) {
        if (isFull()) {
            queue[rear] = data;
            rear = (rear + 1) % 5;
            size++;
        }

    }

    // remove from the queue
    public int dequeue() {
        int data = queue[front];
        if (!isEmpty()) {
            front = (front + 1) % 5;
            size--;
        }
        return data;
    }

    public void show() {
        System.out.println("Elements");
        for (int i = 0; i < size; i++) {
            System.out.println(queue[(front + i) % 5] + " ");
        }
    }

    public int getSize() {
        return size;
    }

    public boolean isEmpty() {
        return getSize() == 0;
    }

    public boolean isFull() {
        return size == 5;
    }
}
