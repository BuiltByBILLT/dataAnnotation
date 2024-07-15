import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Arrays;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
      try {
    // Configuration: Read inputs and set up adjacency matrix
    Scanner fileScan = new Scanner(new File("txt/bfsdfs.txt"));
    boolean directed = fileScan.nextInt() == 1;
    int numV = fileScan.nextInt();
    int numE = fileScan.nextInt();
    fileScan.nextLine();
    String vertices[] = fileScan.nextLine().split(" ");
    String edges[] = fileScan.nextLine().split(" ");
    int adjMatrix[][] = new int[numV][numV];

    for (String edge : edges) {
        char left = edge.charAt(0);
        char right = edge.charAt(1);
        adjMatrix[left - 'A'][right - 'A'] = 1;
        if (!directed) {
            adjMatrix[right - 'A'][left - 'A'] = 1;
        }
    }
    int startIdx = fileScan.next().charAt(0) - 'A';
    fileScan.close();

    // Initialize order array, queue, and visited list
    char[] order = new char[numV];
    Arrays.fill(order, '-');
    order[0] = (char) ('A' + startIdx);
    LinkedList queue = new LinkedList(new Node(startIdx, null));
    LinkedList visited = new LinkedList(new Node(startIdx, null));

    // BFS Logic
    int index = 1;
    while (index != numV) {
        int current = queue.getDataAtIndex(0);
        queue.removeNodeAtIndex(0);
        for (int i = 0; i < numV; i++) {
            if (adjMatrix[current][i] == 1 && !visited.contains(i)) {
                order[index++] = (char) ('A' + i);
                queue.addLast(new Node(i, null));
                visited.addLast(new Node(i, null));
            }
        }
    }

    // Print result
    printVertices(order);
} catch (FileNotFoundException fnfe) {
    fnfe.printStackTrace();
}
              
    }

    static void printVertices(char[] order) {
        for (char vertex : order) {
            if (vertex != '-') {
                System.out.print(vertex + " ");
            }
        }
        System.out.println();
    }
}
