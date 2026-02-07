
import numpy as np

def inject_anomalies(data, n_rows):
    anomaly_flags = np.zeros(n_rows)
    for i in range(0, n_rows, 5000):
        end = min(i+200, n_rows)
        data[i:end] += np.random.normal(5, 1, size=data[i:end].shape)
        anomaly_flags[i:end] = 1
    return data, anomaly_flags
