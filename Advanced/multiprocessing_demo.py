import time
import multiprocessing
import os

# --- Configuration ---
NUM_TASKS = 8 # Number of heavy calculations to perform
TASK_SIZE = 10**7 # large the calculation is (higher = more CPU time)

# --- The CPU-Bound Task ---
def heavy_calculation(n):
    """Calculates the sum of squares up to 'n', simulating a heavy workload."""
    result = 0
    for i in range(n):
        result += i * i
    # print(f"Process {os.getpid()}: Finished calculation up to {n}")
    return result

# --- 1. Sequential Execution (Baseline) ---
def run_sequential():
    start_time = time.perf_counter()
    print("Starting Sequential execution...")
    
    # Run the heavy calculation one after the other
    results = [heavy_calculation(TASK_SIZE) for _ in range(NUM_TASKS)]
    
    end_time = time.perf_counter()
    return end_time - start_time

# --- 2. Multiprocessing Execution ---
def run_multiprocessing():
    # It's best to set max_workers to the number of CPU cores
    MAX_CORES = os.cpu_count() or 4
    
    start_time = time.perf_counter()
    print(f"Starting Multiprocessing execution with up to {MAX_CORES} cores...")
    
    # Use ProcessPoolExecutor to manage a pool of worker processes
    with multiprocessing.Pool(processes=MAX_CORES) as pool:
        # Use map to distribute the heavy_calculation function across all tasks
        # The list comprehension creates the list of arguments (TASK_SIZE) for each run
        tasks_args = [TASK_SIZE] * NUM_TASKS
        results = pool.map(heavy_calculation, tasks_args)
        
    end_time = time.perf_counter()
    return end_time - start_time

# --- Main Execution ---
if __name__ == "__main__":
    # The if __name__ == "__main__": block is crucial for multiprocessing on Windows/macOS.
    
    # Run the sequential version
    time_sequential = run_sequential()
    print(f"Sequential Time:    {time_sequential:.4f} seconds\n")
    
    # Run the multiprocessing version
    time_multiprocessing = run_multiprocessing()
    print(f"Multiprocessing Time: {time_multiprocessing:.4f} seconds")
    
    # Calculate the benefit
    if time_multiprocessing > 0:
        benefit = time_sequential / time_multiprocessing
        print(f"\n **Benefit:** Multiprocessing was approximately {benefit:.2f}x faster.")