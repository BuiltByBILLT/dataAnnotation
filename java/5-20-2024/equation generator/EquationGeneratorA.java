import java.util.Scanner;

public class EquationGeneratorA {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] inputValues = scanner.nextLine().split(" ");

        int[] input = new int[inputValues.length];
        for (int i = 0; i < inputValues.length; i++) {
            input[i] = Integer.parseInt(inputValues[i]);
        }

        int smallestPositive = findSmallestPositive(input);
        System.out.println(smallestPositive);
    }

    public static int findSmallestPositive(int[] input) {
        // Optimization: Start searching from the sum of all positive numbers.
        // This is the smallest possible value that can be achieved.
        int smallestPositive = 0;
        // for (int num : input) {
        //     if (num > 0) {
        //         smallestPositive += num;
        //     }
        // }
        System.out.println("smallestPositive: " + smallestPositive);

        // If the smallest possible sum is 0, it means there were no positive numbers.
        // if (smallestPositive == 0) {
        //     return 1; // The default smallest positive number.
        // }

        while (true) {
            if (checkEquations(input, 0, 0, smallestPositive)) {
                return smallestPositive;
            }
            
            // Optimization: Increase smallestPositive by the minimum positive number in the input.
            // This speeds up the search for larger arrays.
            int minPositiveIncrement = findMinPositive(input);
            System.out.println("minPositiveIncrement: " + minPositiveIncrement);
            smallestPositive += minPositiveIncrement;
        }
    }

    public static boolean checkEquations(int[] input, int index, int currentSum, int target) {
        if (index == input.length) {
            return currentSum == target;
        }

        int number = input[index];

        if (checkEquations(input, index + 1, currentSum + number, target)) {
            return true;
        }
        if (checkEquations(input, index + 1, currentSum - number, target)) {
            return true;
        }

        return false;
    }

    private static int findMinPositive(int[] input) {
        int minPositive = Integer.MAX_VALUE;
        for (int num : input) {
            if (num > 0 && num < minPositive) {
                minPositive = num;
            }
        }
        return minPositive;
    }
}