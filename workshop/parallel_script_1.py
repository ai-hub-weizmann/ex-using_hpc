import numpy as np
import multiprocessing as mp
import time
import sys

def slow_function(_):
    """A simple function that runs slower in Jupyter."""
    np.random.seed()  # Avoid repeatability in multiprocessing
    A = np.random.rand(1000, 1000)
    B = np.random.rand(1000, 1000)
    return np.linalg.slogdet(A @ B)[1]  # Compute the log determinant

if __name__ == "__main__":
    num_tasks = 10  # Reduce in Jupyter, increase in a script

    start = time.time()
    
    # Detect if running in Jupyter
    in_jupyter = "ipykernel" in sys.modules

    if in_jupyter:
        # Simulate overhead in Jupyter (worse multiprocessing performance)
        results = list(map(slow_function, range(num_tasks)))
    else:
        # Efficient multiprocessing in script mode
        with mp.Pool(processes=mp.cpu_count()) as pool:
            results = pool.map(slow_function, range(num_tasks))

    end = time.time()
    
    print(f"Time taken: {end - start:.2f} seconds")
    print(f"Sum of results: {sum(results)}")
