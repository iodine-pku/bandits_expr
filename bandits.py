import numpy as np
from abc import ABC, abstractmethod
from typing import List, Tuple, Optional

class BanditArm(ABC):
    """Abstract base class for bandit arms with different distributions."""
    @abstractmethod
    def pull(self) -> float:
        """Pull the arm and get a reward."""
        pass

    @abstractmethod
    def get_expected_reward(self) -> float:
        """Get the true expected reward of the arm."""
        pass

class BernoulliArm(BanditArm):
    def __init__(self, p: float):
        self.p = p
        
    def pull(self) -> float:
        return float(np.random.binomial(1, self.p))
    
    def get_expected_reward(self) -> float:
        return self.p

class GaussianArm(BanditArm):
    def __init__(self, mu: float, sigma: float):
        self.mu = mu
        self.sigma = sigma
        
    def pull(self) -> float:
        return float(np.random.normal(self.mu, self.sigma))
    
    def get_expected_reward(self) -> float:
        return self.mu

class StochasticBandit:
    """Multi-armed bandit with stochastic arms."""
    def __init__(self, arms: List[BanditArm]):
        """
        Initialize bandit with a list of arms.
        
        Args:
            arms: List of BanditArm objects
        """
        self.arms = arms
        self.n_arms = len(arms)
       
        # Find optimal arm
        self.optimal_reward = max(arm.get_expected_reward() for arm in arms)
        self.optimal_arm = max(range(self.n_arms), 
                             key=lambda i: arms[i].get_expected_reward())
    
    def pull(self, arm_index: int) -> float:
        """Pull the specified arm and return reward."""
        if not 0 <= arm_index < self.n_arms:
            raise ValueError(f"Arm index must be between 0 and {self.n_arms-1}")
        return self.arms[arm_index].pull()
    
    def get_optimal_arm(self) -> int:
        """Return the index of the optimal arm."""
        return self.optimal_arm
    
    def get_optimal_reward(self) -> float:
        """Return the expected reward of the optimal arm."""
        return self.optimal_reward
