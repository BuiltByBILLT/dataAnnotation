import pandas as pd
from models.reward_allocation.allocation_problem import AllocationProblem, Customer
from models.reward_allocation.feasibility_checker import FeasibilityChecker

class ImprovedHeuristic:
    def __init__(self, problem: AllocationProblem, max_iterations: int = 1000):
        self.problem = problem
        self.max_iterations = max_iterations

    def allocate_rewards(self) -> pd.DataFrame:
        """Allocates rewards to customers using an improved heuristic approach."""

        solution = pd.DataFrame(columns=["customer_uuid", "reward_uuid", "estimated_spend"])
        iteration = 0

        while not FeasibilityChecker.is_feasible(solution, self.problem) and iteration < self.max_iterations:
            # Prioritize customers with highest redemption probabilities
            sorted_customers = sorted(self.problem.customer_set, 
                                      key=lambda c: c.get_max_redemption_probability(), 
                                      reverse=True)

            for customer in sorted_customers:
                # Find the reward with the highest redemption probability for this customer
                best_reward = max(self.problem.reward_set, 
                                  key=lambda r: customer.get_redemption_probability(r))

                # Check if allocating this reward is feasible
                temp_solution = solution.copy()
                temp_solution = temp_solution.append({"customer_uuid": customer.customer_uuid,
                                                      "reward_uuid": best_reward.reward_uuid,
                                                      "estimated_spend": best_reward.estimated_spend},
                                                      ignore_index=True)
                
                if FeasibilityChecker.is_feasible(temp_solution, self.problem):
                    solution = temp_solution
                
            iteration += 1

        return solution
                  