import os
import multiprocessing
import time

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_in_range(start, end):
    """Count prime numbers in a given range."""
    count = sum(1 for num in range(start, end) if is_prime(num))
    return count

if __name__ == "__main__":
    num_cores = ncpus = int(os.getenv("LSB_DJOB_NUMPROC", os.cpu_count()))  # Use up to 10 cores
    pool = multiprocessing.Pool(num_cores)

    start_time = time.time()

    # Define a large range to keep the computation running for a few minutes
    num_range = 10**6  
    step = num_range // num_cores

    # Create tasks for each CPU core
    tasks = [(i * step, (i + 1) * step) for i in range(num_cores)]

    # Run in parallel
    results = pool.starmap(count_primes_in_range, tasks)
    
    pool.close()
    pool.join()

    total_primes = sum(results)
    elapsed_time = time.time() - start_time

    print(f"Total prime numbers found: {total_primes}")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
