import java.util.Scanner;

public class EquationGeneratorB {

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
        int totalSum = 0;
        for (int value : input) {
            totalSum += Math.abs(value); // Assuming all possible values are reachable.
        }
        
        for (int target = 1; target <= totalSum; target++) {
            if (checkEquations(input, 0, 0, target)) {
                return target;
            }
        }
        return totalSum + 1; // If none of the numbers 1 through totalSum are reachable, return totalSum + 1.
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
}