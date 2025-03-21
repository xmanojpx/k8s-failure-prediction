import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

class K8sMetricsSimulator:
    def __init__(self, num_nodes=5, num_pods=20):
        self.num_nodes = num_nodes
        self.num_pods = num_pods
        
    def generate_normal_metrics(self):
        """Generate normal operating metrics"""
        return {
            'cpu_usage': random.uniform(20, 60),
            'memory_usage': random.uniform(30, 70),
            'network_io': random.uniform(100, 500),
            'disk_usage': random.uniform(40, 70),
            'pod_restarts': random.randint(0, 2),
            'response_time': random.uniform(0.1, 0.5)
        }
    
    def generate_anomalous_metrics(self):
        """Generate metrics indicating potential issues"""
        return {
            'cpu_usage': random.uniform(85, 100),
            'memory_usage': random.uniform(85, 100),
            'network_io': random.uniform(800, 1000),
            'disk_usage': random.uniform(85, 100),
            'pod_restarts': random.randint(3, 10),
            'response_time': random.uniform(1.0, 5.0)
        }
    
    def generate_dataset(self, hours=24, interval_minutes=5):
        """Generate a dataset with both normal and anomalous data"""
        timestamps = pd.date_range(
            start=datetime.now() - timedelta(hours=hours),
            end=datetime.now(),
            freq=f'{interval_minutes}min'
        )
        
        data = []
        for ts in timestamps:
            for node_id in range(self.num_nodes):
                # 10% chance of generating anomalous data
                is_anomaly = random.random() < 0.1
                metrics = self.generate_anomalous_metrics() if is_anomaly else self.generate_normal_metrics()
                
                record = {
                    'timestamp': ts,
                    'node_id': f'node-{node_id}',
                    'is_failure': 1 if is_anomaly else 0,
                    **metrics
                }
                data.append(record)
        
        return pd.DataFrame(data)

def main():
    # Initialize simulator
    simulator = K8sMetricsSimulator()
    
    # Generate dataset
    print("Generating dataset...")
    df = simulator.generate_dataset()
    
    # Save to CSV
    output_file = 'k8s_metrics.csv'
    df.to_csv(output_file, index=False)
    print(f"Dataset saved to {output_file}")
    
    # Print some statistics
    print("\nDataset Statistics:")
    print(f"Total records: {len(df)}")
    print(f"Failure cases: {df['is_failure'].sum()}")
    print(f"Normal cases: {len(df) - df['is_failure'].sum()}")

if __name__ == "__main__":
    main() 