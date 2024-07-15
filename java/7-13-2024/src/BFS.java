import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class BFS {
    public static void main(String[] args) {
        try {
            File file = new File("txt/bfsdfs.txt");
            Scanner scanner = new Scanner(file);

            int numVertices = scanner.nextInt();
            int numEdges = scanner.nextInt();
            boolean directed = scanner.nextInt() == 1;

            int[][] adjacencyMatrix = new int[numVertices][numVertices];
            for (int i = 0; i < numEdges; i++) {
                int from = scanner.next().charAt(0) - 'A';
                int to = scanner.next().charAt(0) - 'A';
                adjacencyMatrix[from][to] = 1;
                if (!directed) {
                    adjacencyMatrix[to][from] = 1;
                }
            }

            int startVertex = scanner.next().charAt(0) - 'A';

            char[] order = new char[numVertices];
            for (int i = 0; i < numVertices; i++) {
                order[i] = '-';
            }
            order[0] = (char) ('A' + startVertex);

            LinkedList queue = new LinkedList(new Node(startVertex, null));
            LinkedList visited = new LinkedList(new Node(startVertex, null));

            int index = 1;
            while (index != numVertices) {
                int current = queue.getDataAtIndex(0);
                queue.removeNodeAtIndex(0);
                for (int i = 0; i < numVertices; i++) {
                    if (adjacencyMatrix[current][i] == 1 && !visited.contains(i)) {
                        order[index] = (char) ('A' + i);
                        index++;
                        queue.addLast(new Node(i, null));
                        visited.addLast(new Node(i, null));
                    }
                }
            }

            printVertices(order);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}