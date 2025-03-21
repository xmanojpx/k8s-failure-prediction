import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_cpu_usage(data):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x='timestamp', y='cpu_usage', marker='o')
    plt.title('CPU Usage Over Time')
    plt.xlabel('Time')
    plt.ylabel('CPU Usage (%)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('cpu_usage_plot.png')
    plt.show()

def plot_memory_usage(data):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x='timestamp', y='memory_usage', marker='o', color='orange')
    plt.title('Memory Usage Over Time')
    plt.xlabel('Time')
    plt.ylabel('Memory Usage (MB)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('memory_usage_plot.png')
    plt.show()

def plot_network_io(data):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x='timestamp', y='network_io', marker='o', color='green')
    plt.title('Network IO Over Time')
    plt.xlabel('Time')
    plt.ylabel('Network IO (KB/s)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('network_io_plot.png')
    plt.show()

def plot_pod_status(data):
    plt.figure(figsize=(12, 6))
    sns.countplot(data=data, x='pod_status', palette='Set2')
    plt.title('Pod Status Distribution')
    plt.xlabel('Pod Status')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('pod_status_distribution.png')
    plt.show()

def main():
    # Load the processed training data
    data = pd.read_csv('../data/processed/training_data.csv')
    
    # Plot metrics
    plot_cpu_usage(data)
    plot_memory_usage(data)
    plot_network_io(data)
    plot_pod_status(data)

if __name__ == "__main__":
    main()