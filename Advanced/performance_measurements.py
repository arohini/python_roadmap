import time
import threading
import multiprocessing
import asyncio
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# --- Configuration ---
NUM_TASKS = 10
IO_SLEEP_DURATION = 0.5  # Time for I/O-Bound Task (e.g., waiting for network)
CPU_ITERATIONS = 5000000  # Intensity for CPU-Bound Task (heavy calculation)

# --- 1. The I/O-Bound Task (Optimized by Multithreading/AsyncIO) ---
def io_bound_task(task_id):
    """A blocking function simulating waiting for an external resource."""
    time.sleep(IO_SLEEP_DURATION)
    return f"I/O Task {task_id} done"

async def async_io_bound_task(task_id):
    """An awaitable function that yields control during waiting."""
    await asyncio.sleep(IO_SLEEP_DURATION)
    return f"Async Task {task_id} done"

# --- 2. The CPU-Bound Task (Optimized by Multiprocessing) ---
def cpu_bound_task(task_id):
    """A function performing heavy calculation without I/O."""
    count = 0
    for i in range(CPU_ITERATIONS):
        count += i * i
    return f"CPU Task {task_id} done"

# =================================================================
#                         I/O-BOUND COMPARISONS
# =================================================================

def run_io_sequential():
    start_time = time.perf_counter()
    [io_bound_task(i) for i in range(NUM_TASKS)]
    end_time = time.perf_counter()
    return end_time - start_time

def run_io_multithreading():
    start_time = time.perf_counter()
    with ThreadPoolExecutor(max_workers=NUM_TASKS) as executor:
        list(executor.map(io_bound_task, range(NUM_TASKS)))
    end_time = time.perf_counter()
    return end_time - start_time

async def run_io_asyncio_tasks():
    tasks = [async_io_bound_task(i) for i in range(NUM_TASKS)]
    await asyncio.gather(*tasks)

def run_io_asyncio():
    start_time = time.perf_counter()
    asyncio.run(run_io_asyncio_tasks())
    end_time = time.perf_counter()
    return end_time - start_time

# =================================================================
#                        CPU-BOUND COMPARISON
# =================================================================

def run_cpu_sequential():
    start_time = time.perf_counter()
    [cpu_bound_task(i) for i in range(NUM_TASKS)]
    end_time = time.perf_counter()
    return end_time - start_time

def run_cpu_multiprocessing():
    start_time = time.perf_counter()
    # Use max_workers up to the number of CPU cores for best results
    max_cores = os.cpu_count() or 4
    with ProcessPoolExecutor(max_workers=max_cores) as executor:
        list(executor.map(cpu_bound_task, range(NUM_TASKS)))
    end_time = time.perf_counter()
    return end_time - start_time

# =================================================================
#                            MAIN EXECUTION
# =================================================================

def main():
    print(f"--- Running {NUM_TASKS} Tasks ---")
    
    # Ensure Multiprocessing uses a safe start method on all OSs
    if multiprocessing.get_start_method(allow_none=True) is None:
        multiprocessing.set_start_method("spawn", force=True)

    ## 🗃️ I/O-Bound Task Comparison (Waiting)
    print("\n--- I/O-Bound Task (0.5s Wait) ---")
    
    time_seq = run_io_sequential()
    print(f"1. Sequential Time:    {time_seq:.4f} seconds (Baseline)")
    
    time_mt = run_io_multithreading()
    print(f"2. Multithreading Time: {time_mt:.4f} seconds")
    print(f"   --> Benefit: {time_seq/time_mt:.2f}x faster")
    
    time_async = run_io_asyncio()
    print(f"3. AsyncIO Time:        {time_async:.4f} seconds")
    print(f"   --> Benefit: {time_seq/time_async:.2f}x faster")
    
    # Multiprocessing is often slower than MT/Async for I/O due to overhead, but still better than sequential
    time_mp_io = run_cpu_multiprocessing() 
    print(f"4. Multiprocessing Time: {time_mp_io:.4f} seconds (Note: High overhead for I/O)")
    print(f"   --> Benefit: {time_seq/time_mp_io:.2f}x faster")
    
    
    ## 🧠 CPU-Bound Task Comparison (Calculating)
    print("\n--- CPU-Bound Task (Heavy Calculation) ---")
    
    time_seq_cpu = run_cpu_sequential()
    print(f"1. Sequential Time:     {time_seq_cpu:.4f} seconds (Baseline)")
    
    time_mt_cpu = run_io_multithreading() # Using MT here just to show the contrast
    print(f"2. Multithreading Time: {time_mt_cpu:.4f} seconds (Expected negligible gain or loss due to GIL)")

    time_mp_cpu = run_cpu_multiprocessing()
    print(f"3. Multiprocessing Time: {time_mp_cpu:.4f} seconds")
    print(f"   --> Benefit: {time_seq_cpu/time_mp_cpu:.2f}x faster (True Parallelism)")


if __name__ == "__main__":
    main()