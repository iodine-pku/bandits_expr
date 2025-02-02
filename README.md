# Multi-Armed Bandit Experiments

This repository provides a flexible framework for experimenting with various multi-armed bandit algorithms. It includes implementations of several classic algorithms such as ε-greedy, UCB1, and Explore-Then-Exploit, along with both Gaussian and Bernoulli bandit environments.

The framework allows you to:
- Compare different bandit algorithms under various settings
- Visualize algorithm performance through regret and optimal arm selection plots
- Easily extend with new algorithms and bandit environments
- Configure experiments without coding through a simple configuration file

## Quick Start for Non-Programmers

If you're interested in running experiments without coding, you can directly modify the `configs.py` file. This file contains predefined experiment configurations that you can adjust.

### Modifying Configurations

In `configs.py`, each configuration specifies:
- The type and parameters of bandit arms
- The algorithms to compare and their parameters
- Number of rounds and experimental runs
- Random seed for reproducibility

Example configuration:
```python
"epsilon_comparison_low_variance": {
    "name": "Epsilon Comparison (Low Variance)",
    "arms_config": {
        "type": "gaussian",
        "params": [
            {"mu": 0.3, "sigma": 0.1},
            {"mu": 0.5, "sigma": 0.1},
            {"mu": 0.7, "sigma": 0.1},  
        ]
    },
    "algorithms_config": [
        {"name": "EpsilonGreedy", "params": {"epsilon": 0.0}},
        {"name": "EpsilonGreedy", "params": {"epsilon": 0.01}},
        {"name": "EpsilonGreedy", "params": {"epsilon": 0.1}},
    ],
    "n_rounds": 1000,
    "n_runs": 50,
    "seed": 42
}
```

You can modify:
- `mu` and `sigma` for Gaussian arms (or `p` for Bernoulli arms)
- Algorithm parameters (e.g., `epsilon` for ε-greedy)
- Number of rounds (`n_rounds`) and runs (`n_runs`)
- Add or remove algorithms to compare

## Extending the Framework

### Adding New Bandit Arms

To add a new type of bandit arm:

1. Create a new class in `bandits.py` inheriting from `BanditArm`
2. Implement the required methods:
   - `pull()`: Return a reward when the arm is pulled
   - `get_expected_reward()`: Return the true expected reward

Example:
```python
class CustomArm(BanditArm):
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
    
    def pull(self) -> float:
        # Implement reward generation logic
        return reward
    
    def get_expected_reward(self) -> float:
        # Return true expected reward
        return expected_reward
```

### Adding New Algorithms

To add a new bandit algorithm:

1. Create a new class in `algorithms.py` inheriting from `BanditAlgorithm`
2. Implement the required methods:
   - `select_arm()`: Choose which arm to pull next
   - Optionally override `update()` if needed

Example:
```python
class CustomAlgorithm(BanditAlgorithm):
    def __init__(self, n_arms: int, custom_param: float):
        super().__init__(n_arms)
        self.custom_param = custom_param
    
    def select_arm(self) -> int:
        # Implement arm selection logic
        return chosen_arm
```

## Running Experiments

### Environment Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Experiments
First, ensure you're at the root of this repository.

To run all configured experiments:
```bash
python main.py
```

The results will be saved as plots in the `plots/` directory, with one PDF file per configuration group. Each plot shows:
- Cumulative regret over time
- Percentage of optimal arm pulls over time

For each metric, the plots show both the mean and standard deviation across multiple runs.

### More Resources
- [https://cse442-17f.github.io/LinUCB/](https://cse442-17f.github.io/LinUCB/) for interactive exploration on the Web and some heuristic intuition about algorithm choices.
- [Algorithms for the Multi-Armed Bandit Problem](https://www.jmlr.org/papers/volume1/kuleshov00a/kuleshov00a.pdf) - Comprehensive experimental analysis of various bandit algorithms. (Kuleshov & Precup, JMLR 2000)
