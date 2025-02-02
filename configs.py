# configs.py

# Feel free to add more configurations or modify the existing ones
# Can also be imported from a JSON or YAML file
CONFIGS = {
    "epsilon_comparison_high_variance": {
        "name": "Epsilon Comparison (High Variance)",
        "arms_config": {
            "type": "gaussian",
            "params": [
                {"mu": 0.3, "sigma": 1},
                {"mu": 0.5, "sigma": 1},
                {"mu": 0.7, "sigma": 1},  
            ]
        },
        "algorithms_config": [
            {"name": "EpsilonGreedy", "params": {"epsilon": 0.0}},
            {"name": "EpsilonGreedy", "params": {"epsilon": 0.01}},
            {"name": "EpsilonGreedy", "params": {"epsilon": 0.1}},
            {"name": "DecayingEpsilonGreedy", "params": {"initial_epsilon": 0.2}},
        ],
        "n_rounds": 1000,
        "n_runs": 50,
        "seed": 42
    },

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
            {"name": "DecayingEpsilonGreedy", "params": {"initial_epsilon": 0.2}},
        ],
        "n_rounds": 1000,
        "n_runs": 50,
        "seed": 42
    },

    "algorithm_comparison_high_variance": {
        "name": "Algorithm Comparison (High Variance)",
        "arms_config": {
            "type": "gaussian",
            "params": [
                {"mu": 0.3, "sigma": 1},
                {"mu": 0.5, "sigma": 1},
                {"mu": 0.7, "sigma": 1},  # Clearly optimal
            ]
        },
        "algorithms_config": [
            {"name": "UCB1", "params": {"C": 2.0}},
            {"name": "EpsilonGreedy", "params": {"epsilon": 0.2}},
            {"name": "ETE", "params": {"explore_rounds": 100, "uniform_random": True}},
        ],
        "n_rounds": 1000,
        "n_runs": 50,
        "seed": 42
    },

    "algorithm_comparison_low_variance": {
        "name": "Algorithm Comparison (Low Variance)",
        "arms_config": {
            "type": "gaussian",
            "params": [
                {"mu": 0.3, "sigma": 0.1},
                {"mu": 0.5, "sigma": 0.1},
                {"mu": 0.7, "sigma": 0.1},  
            ]
        },
        "algorithms_config": [
            {"name": "UCB1", "params": {"C": 2.0}},
            {"name": "EpsilonGreedy", "params": {"epsilon": 0.2}},
            {"name": "ETE", "params": {"explore_rounds": 100, "uniform_random": True}},
        ],
        "n_rounds": 1000,
        "n_runs": 50,
        "seed": 42
    },
}