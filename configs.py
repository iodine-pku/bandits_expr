# configs.py

# Common bandit scenarios
# Can also be imported from a JSON or YAML file
CONFIGS = {
    "epsilon_comparison_easy": {
        "name": "Epsilon Comparison (Easy)",
        "arms_config": {
            "type": "gaussian",
            "params": [
                {"mu": 0.2, "sigma": 0.1},
                {"mu": 0.3, "sigma": 0.1},
                {"mu": 0.4, "sigma": 0.1},
                {"mu": 0.8, "sigma": 0.1},  # Clearly optimal
            ]
        },
        "algorithms_config": [
            {"name": "EpsilonGreedy", "params": {"epsilon": 0.0}},
            {"name": "EpsilonGreedy", "params": {"epsilon": 0.01}},
            {"name": "EpsilonGreedy", "params": {"epsilon": 0.1}},
            {"name": "DecayingEpsilonGreedy", "params": {"initial_epsilon": 1.0}},
        ],
        "n_rounds": 1000,
        "seed": 42
    },

    "epsilon_comparison_hard": {
        "name": "Epsilon Comparison (Hard)",
        "arms_config": {
            "type": "gaussian",
            "params": [
                {"mu": 0.45, "sigma": 0.1},
                {"mu": 0.47, "sigma": 0.1},
                {"mu": 0.49, "sigma": 0.1},
                {"mu": 0.50, "sigma": 0.1},  # Barely optimal
            ]
        },
        "algorithms_config": [
            {"name": "EpsilonGreedy", "params": {"epsilon": 0.0}},
            {"name": "EpsilonGreedy", "params": {"epsilon": 0.01}},
            {"name": "EpsilonGreedy", "params": {"epsilon": 0.1}},
            {"name": "DecayingEpsilonGreedy", "params": {"initial_epsilon": 1.0}},
        ],
        "n_rounds": 1000,
        "seed": 42
    },

    "algorithm_comparison_easy": {
        "name": "Algorithm Comparison (Easy)",
        "arms_config": {
            "type": "gaussian",
            "params": [
                {"mu": 0.2, "sigma": 0.1},
                {"mu": 0.3, "sigma": 0.1},
                {"mu": 0.4, "sigma": 0.1},
                {"mu": 0.8, "sigma": 0.1},  # Clearly optimal
            ]
        },
        "algorithms_config": [
            {"name": "UCB1", "params": {"C": 2.0}},
            {"name": "DecayingEpsilonGreedy", "params": {"initial_epsilon": 1.0}},
            {"name": "ETE", "params": {"explore_rounds": 100, "uniform_random": True}},
        ],
        "n_rounds": 1000,
        "seed": 42
    },

    "algorithm_comparison_hard": {
        "name": "Algorithm Comparison (Hard)",
        "arms_config": {
            "type": "gaussian", 
            "params": [
                {"mu": 0.45, "sigma": 0.1},
                {"mu": 0.47, "sigma": 0.1},
                {"mu": 0.49, "sigma": 0.1},
                {"mu": 0.50, "sigma": 0.1},  # Barely optimal
            ]
        },
        "algorithms_config": [
            {"name": "UCB1", "params": {"C": 2.0}},
            {"name": "DecayingEpsilonGreedy", "params": {"initial_epsilon": 1.0}},
            {"name": "ETE", "params": {"explore_rounds": 100, "uniform_random": True}},
        ],
        "n_rounds": 1000,
        "seed": 42
    },
}