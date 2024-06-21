import logging 
import pandas as pd 
from typing import List
# from allocation_problem import AllocationProblem, Customer
logger = logging.getLogger(__name__)



class Customer:
    def __init__(self, customer_uuid: str):
        self.customer_uuid = customer_uuid

class AllocationProblem:
    def __init__(self, customers: List[Customer], max_estimated_spend: float, max_estimated_spend_per_customer: float, max_rewards_per_customer: int, min_rewards_per_customer: int):
        self.customers = customers
        self.max_estimated_spend = max_estimated_spend
        self.max_estimated_spend_per_customer = max_estimated_spend_per_customer
        self.max_rewards_per_customer = max_rewards_per_customer
        self.min_rewards_per_customer = min_rewards_per_customer


class FeasibilityChecker:
    """Holds methods for checking the feasibility of heuristic solutions."""

    @staticmethod
    def is_full_customer_set_present(solution: pd.DataFrame, customer_set: List['Customer']) -> bool:
        """Check that all customer uuids are present in the solution."""
        return set(solution["customer_uuid"]) == {c.customer_uuid for c in customer_set}

    @staticmethod
    def is_total_spend_respected(solution: pd.DataFrame, max_estimated_spend: float) -> bool:
        """Check that total spend does not exceed limit."""
        total_spend = solution["estimated_spend"].sum()
        return total_spend <= max_estimated_spend  # type: ignore[no-any-return]

    @staticmethod
    def is_spend_per_customer_respected(solution: pd.DataFrame, max_estimated_spend_per_customer: float) -> bool:
        """Check that spend per customer does not exceed limit."""
        max_spend_customer = solution.groupby("customer_uuid")["estimated_spend"].sum().max()
        return max_spend_customer <= max_estimated_spend_per_customer  # type: ignore[no-any-return]

    @staticmethod
    def is_max_rewards_per_customer_respected(solution: pd.DataFrame, max_rewards_per_customer: int) -> bool:
        """Check that no customer is allocated more than max number of rewards."""
        max_rewards = solution.groupby("customer_uuid")["reward_uuid"].count().max()
        return max_rewards <= max_rewards_per_customer  # type: ignore[no-any-return]

    @staticmethod
    def is_min_rewards_per_customer_respected(solution: pd.DataFrame, min_rewards_per_customer: int) -> bool:
        """Check that no customer allocated less than the min number of rewards."""
        min_rewards = solution.groupby("customer_uuid")["reward_uuid"].count().min()
        return min_rewards >= min_rewards_per_customer  # type: ignore[no-any-return]

    @staticmethod
    def is_max_allocations_per_reward_respected(solution: pd.DataFrame, instance: 'AllocationProblem') -> bool:
        """Check that no reward is allocated more than its maximum number of allocations."""
        allocations_by_reward = solution.groupby("reward_uuid")["customer_uuid"].count()
        for reward_uuid, allocation_count in allocations_by_reward.items():
            max_allocations = instance.get_reward_attribute_from_uuid(reward_uuid, "max_allocations")
            if allocation_count > max_allocations:
                logging.warning(
                    f"Reward {reward_uuid} exceeds max allocations."
                    f" allocated: {allocation_count}, max: {max_allocations}"
                )
                return False
        return True

    @staticmethod
    def is_only_one_reward_per_target_assigned(solution: pd.DataFrame, instance: 'AllocationProblem') -> bool:
        """Check that only one reward per target is assigned to a customer."""
        solution_dict = solution.groupby("customer_uuid")["reward_uuid"].apply(set).to_dict()
        for customer in solution_dict:
            assigned_rewards = solution_dict[customer]
            for reward in assigned_rewards:
                overlapping_rewards = instance.reward_target_overlap_mapping[reward]
                if len(assigned_rewards.intersection(overlapping_rewards)) > 1:
                    return False
        return True

    @staticmethod
    def is_feasible(  # pylint: disable=too-many-return-statements
        solution: pd.DataFrame, instance: 'AllocationProblem'
    ) -> bool:
        """Determine whether a solution is feasible given the problem definition."""
        max_rewards_per_customer = instance.decision_parameters.max_rewards_per_customer
        min_rewards_per_customer = instance.decision_parameters.min_rewards_per_customer
        max_estimated_spend_per_customer = instance.decision_parameters.max_estimated_spend_per_customer
        max_estimated_spend = instance.decision_parameters.max_estimated_spend

        if (min_rewards_per_customer >= 1) and (
            not FeasibilityChecker.is_full_customer_set_present(solution, instance.customer_set)
        ):
            logger.warning("Not all customers present in solution")
            customer_set_size = len(instance.customer_set)
            n_customers_in_solution = len(set(solution["customer_uuid"]))
            logger.warning(f"Size of customer set: {customer_set_size}, present in solution: {n_customers_in_solution}")
            return False
        elif not FeasibilityChecker.is_total_spend_respected(solution, max_estimated_spend):
            logger.warning("Total estimated spend exceeds limit")
            return False
        elif not FeasibilityChecker.is_spend_per_customer_respected(solution, max_estimated_spend_per_customer):
            logger.warning("Customer estimated spend exceeds limit")
            return False
        elif not FeasibilityChecker.is_max_rewards_per_customer_respected(solution, max_rewards_per_customer):
            logger.warning("Number of rewards per customer exceeds allowed maximum")
            return False
        elif not FeasibilityChecker.is_min_rewards_per_customer_respected(solution, min_rewards_per_customer):
            logger.warning("Number of rewards per customer under required minimum")
            return False
        elif not FeasibilityChecker.is_max_allocations_per_reward_respected(solution, instance):
            logger.warning("Reward allocation more than max_allocations times")
            return False
        elif not FeasibilityChecker.is_only_one_reward_per_target_assigned(solution, instance):
            logger.warning("More than one reward per target assigned")
            return False
        else:
            logger.info("All constraints satisfied")
            return True
