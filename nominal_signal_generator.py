
import numpy as np

def generate_nominal_chunk(n_rows):
    return np.random.normal(0, 1, size=(n_rows, 10))
