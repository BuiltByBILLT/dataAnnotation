# from models.reward_allocation.allocation_problem import AllocationProblem, Customer
from models.reward_allocation.feasibility_checker import FeasibilityChecker, AllocationProblem, Customer
from improvedB import ImprovedHeuristic
import pandas as pd

if __name__ == "__main__":
    # Example usage of ImprovedHeuristic
    customers = [Customer("c1"), Customer("c2"), Customer("c3")]
    instance = AllocationProblem(customers, max_estimated_spend=100, max_estimated_spend_per_customer=50, max_rewards_per_customer=2, min_rewards_per_customer=1)
    heuristic = ImprovedHeuristic(instance, max_iterations=100)
    solution = heuristic.allocate_rewards()
    print(solution)