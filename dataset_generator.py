
from anomaly_engine import inject_anomalies
from nominal_signal_generator import generate_nominal_chunk
import pandas as pd
import os

OUTPUT_DIR = "./generated_dataset"
TOTAL_ROWS = 20000

def generate_dataset():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data = generate_nominal_chunk(TOTAL_ROWS)
    data, events = inject_anomalies(data, TOTAL_ROWS)
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(OUTPUT_DIR, "satellite_dataset.csv"), index=False)

if __name__ == "__main__":
    generate_dataset()
