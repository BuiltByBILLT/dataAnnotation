from models.reward_allocation.feasibility_checker import FeasibilityChecker, AllocationProblem, Customer
import pandas as pd

class ImprovedHeuristic:
    def __init__(self, instance: AllocationProblem, max_iterations: int):
        self.instance = instance
        self.max_iterations = max_iterations

    def generate_solution(self) -> pd.DataFrame:
        """Generates a feasible solution maximizing total redemption probability."""

        solution = pd.DataFrame()  # Initialize empty solution

        for _ in range(self.max_iterations):
            # TODO: Implement your improved heuristic logic here.
            # This should iteratively improve the solution, ensuring feasibility
            # at each step using `FeasibilityChecker.is_feasible(solution, self.instance)`.

            if FeasibilityChecker.is_feasible(solution, self.instance):
                return solution  # Return the first feasible solution found

        # If no feasible solution found within max_iterations, return the last one
        return solution