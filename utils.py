from typing import List, Tuple, Dict
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

def run_experiment(bandit, algorithm, n_rounds: int, n_runs: int = 30, seed: int = None) -> Dict:
    """
    Run a bandit experiment multiple times and collect statistics.
    
    Args:
        - bandit: StochasticBandit instance
        - algorithm: BanditAlgorithm instance
        - n_rounds: Number of rounds per run
        - n_runs: Number of independent runs
        - seed: Random seed for reproducibility
        
    Returns:
        Dictionary containing experimental results
    """

        
    cumulative_rewards = np.zeros((n_runs, n_rounds))
    cumulative_regret = np.zeros((n_runs, n_rounds))
    arm_pulls = np.zeros((n_runs, bandit.n_arms))
    optimal_pulls = np.zeros((n_runs, n_rounds))
    optimal_pulls_percent = np.zeros((n_runs, n_rounds)) # percentage of optimal pulls until round t
    optimal_arm = bandit.optimal_arm
    
    for run in tqdm(range(n_runs)):
        np.random.seed(seed + run)
        algorithm.reset()
        optimal_reward = bandit.get_optimal_reward()
        
        for t in range(n_rounds):
            # Select and pull arm
            arm = algorithm.select_arm()
            reward = bandit.pull(arm)
            
            # Update algorithm
            algorithm.update(arm, reward)
            
            # Record metrics
            cumulative_rewards[run, t] = (
                cumulative_rewards[run, t-1] + reward if t > 0 else reward
            )
            cumulative_regret[run, t] = (
                optimal_reward * (t + 1) - cumulative_rewards[run, t]
            )
            arm_pulls[run, arm] += 1
            optimal_pulls[run, t] = 1 if arm == optimal_arm else 0
            optimal_pulls_percent[run, t] = np.mean(optimal_pulls[run, :t+1])

    results = {
        'avg_reward': np.mean(cumulative_rewards, axis=0),
        'std_reward': np.std(cumulative_rewards, axis=0),
        'avg_regret': np.mean(cumulative_regret, axis=0),
        'std_regret': np.std(cumulative_regret, axis=0),
        'avg_arm_pulls': np.mean(arm_pulls, axis=0),
        'std_arm_pulls': np.std(arm_pulls, axis=0),
        'optimal_pull_percent_mean': np.mean(optimal_pulls_percent, axis=0),
        'optimal_pull_percent_std': np.std(optimal_pulls_percent, axis=0)

    }
    
    return results

def plot_results(results_list: List[Dict], labels: List[str], title: str = "Bandit Algorithm Performance"):
    """Plot results from multiple bandit experiments."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    colors = plt.cm.tab10(np.linspace(0, 1, len(results_list)))
    
    for results, label, color in zip(results_list, labels, colors):
        t = np.arange(len(results['avg_regret']))
        
        # Plot average cumulative regret
        ax1.plot(t, results['avg_regret'], label=label, color=color)
        ax1.fill_between(t,
                        results['avg_regret'] - results['std_regret'],
                        results['avg_regret'] + results['std_regret'],
                        alpha=0.2, color=color)
        
        # Plot optimal arm pull percentage
        ax2.plot(t, results['optimal_pull_percent'], label=label, color=color)
        ax2.fill_between(t,
                        results['optimal_pull_percent'] - results['optimal_pull_percent_std'],
                        results['optimal_pull_percent'] + results['optimal_pull_percent_std'],
                        alpha=0.2, color=color)
    
    ax1.set_title('Cumulative Regret')
    ax1.set_xlabel('Round')
    ax1.set_ylabel('Regret')
    ax1.legend()
    
    ax2.set_title('Optimal Arm Pull Percentage')
    ax2.set_xlabel('Round')
    ax2.set_ylabel('Ratio of Optimal Arm Pulled')
    ax2.legend()
    
    plt.suptitle(title)
    plt.tight_layout()
    return fig