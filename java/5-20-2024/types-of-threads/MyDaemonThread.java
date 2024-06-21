public class MyDaemonThread extends Thread {
    public void run() {
        while (true) {
            System.out.println("Daemon Thread is running...");
            // ... background tasks (e.g., check for updates, logging) ...
        }
    }
    public static void main(String[] args) {
    MyDaemonThread daemonThread = new MyDaemonThread();
    daemonThread.setDaemon(true); // Must be set before starting
    daemonThread.start(); 
    }
}
