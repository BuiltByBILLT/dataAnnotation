import java.util.concurrent.Callable;
import java.util.concurrent.Future;
import java.util.concurrent.Executors;
import java.util.concurrent.ExecutorService;

class MyCallable implements Callable<String> {
    public String call() throws Exception {
        return "Thread " + Thread.currentThread().getId() + " has finished executing";
    }
}

public class ThreadExample3 {
    public static void main(String[] args) throws Exception {
        ExecutorService executor = Executors.newFixedThreadPool(2);
        Future<String> future1 = executor.submit(new MyCallable());
        Future<String> future2 = executor.submit(new MyCallable());

        System.out.println(future1.get());
        System.out.println(future2.get());

        executor.shutdown();
    }
}