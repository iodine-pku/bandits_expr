from abc import ABC, abstractmethod
import numpy as np

class BanditAlgorithm(ABC):
    """Abstract base class for bandit algorithms."""
    def __init__(self, n_arms: int):
        self.n_arms = n_arms
        self.reset()
    
    @abstractmethod
    def select_arm(self) -> int:
        """Select the next arm to pull."""
        pass
    
    def update(self, arm: int, reward: float):
        """Update algorithm's state based on the reward received."""
        self.pulls[arm] += 1
        self.rewards[arm] += reward
        self.t += 1
    
    def reset(self):
        """Reset the algorithm's state."""
        self.pulls = np.zeros(self.n_arms)
        self.rewards = np.zeros(self.n_arms)
        self.t = 0

class EpsilonGreedy(BanditAlgorithm):
    """Epsilon-greedy algorithm with fixed exploration rate."""
    def __init__(self, n_arms: int, epsilon: float = 0.1):
        super().__init__(n_arms)
        self.epsilon = epsilon
    
    def select_arm(self) -> int:
        if np.random.random() < self.epsilon:
            return np.random.randint(self.n_arms)
        
        avg_rewards = np.where(self.pulls > 0, 
                             self.rewards / self.pulls, 
                             float('inf'))
        return int(np.argmax(avg_rewards))

class UCB1(BanditAlgorithm):
    """UCB1 algorithm with parameter C controlling width of confidence intervals."""
    def __init__(self, n_arms: int, C: float = 2.0):
        super().__init__(n_arms)
        self.C = C
    
    def select_arm(self) -> int:
        # Pull each arm once initially
        if self.t < self.n_arms:
            return self.t
        
        # Calculate UCB values with parameter C
        avg_rewards = self.rewards / self.pulls
        ucb_values = avg_rewards + np.sqrt(self.C * np.log(self.t) / self.pulls)
        return int(np.argmax(ucb_values))

class DecayingEpsilonGreedy(EpsilonGreedy):
    """Epsilon-greedy algorithm with decaying exploration rate $\epsilon^{-1/3}$."""
    def __init__(self, n_arms: int, initial_epsilon: float = 1.0):
        super().__init__(n_arms, initial_epsilon)
        self.initial_epsilon = initial_epsilon
    
    def select_arm(self) -> int:
        # Decay epsilon as t^(-1/3)
        current_epsilon = self.initial_epsilon * (self.t + 1) ** (-1/3)
        if np.random.random() < current_epsilon:
            return np.random.randint(self.n_arms)
        
        avg_rewards = np.where(self.pulls > 0, 
                             self.rewards / self.pulls, 
                             float('inf'))
        return int(np.argmax(avg_rewards))

class ETE(BanditAlgorithm):
    """Explore-Then-Exploit algorithm with fixed number of exploration rounds.
     - `uniform_random`: If True, explore rounds are random uniform selection, which is the algorithm defined in the lecture notes.
     Else, explore rounds are divided equally among arms, which is a more common setting in classical texts on bandits."""

    def __init__(self, n_arms: int, explore_rounds: int, uniform_random: bool = False):
        super().__init__(n_arms)
        self.explore_rounds = explore_rounds
        self.explore_per_arm = explore_rounds // n_arms
        self.best_arm = None
        self.uniform_random = uniform_random
    
    def select_arm(self) -> int:
        if self.t < self.explore_rounds:
            if self.uniform_random:
                return np.random.randint(self.n_arms)
            return self.t % self.n_arms
        else:
            if self.best_arm is None:
                avg_rewards = np.where(self.pulls > 0, 
                                     self.rewards / self.pulls, 
                                     float('inf'))
                self.best_arm = int(np.argmax(avg_rewards))
                
            return self.best_arm
        
        