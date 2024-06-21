from typing import List

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