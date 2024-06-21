public class MyUserThread extends Thread {
    public void run() {
        System.out.println("Hello from the User Thread!");
        // ... your thread's tasks ...
    }

    public static void main(String[] args) {
        MyUserThread userThread = new MyUserThread();
        userThread.start();
    }
}