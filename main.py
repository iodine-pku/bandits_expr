from configs import CONFIGS
from utils import *
import matplotlib.pyplot as plt
import os
import sys

def main():
    if not os.path.exists('plots'):
        os.makedirs('plots')

    # Run experiments for each config group
    for group_name, config in CONFIGS.items():
        print(f"\nRunning experiments for {group_name}...")
        plot_config_group(group_name, config)
        plt.close()

if __name__ == "__main__":
    main()