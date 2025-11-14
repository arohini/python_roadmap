import asyncio
import time
import aiohttp # External library for async HTTP requests

# A list of URLs, possibly a much longer list for real-world testing
urls = [
    'https://httpbin.org/delay/1', # Simulates 1 second latency
    'https://httpbin.org/delay/0.5',
    'https://httpbin.org/delay/1.5',
    'https://httpbin.org/delay/0.2'
]

async def fetch_url(session, url):
    """An awaitable coroutine to fetch a URL."""
    start_fetch = time.time()
    print(f"[{time.time()-start_time:.2f}s] Starting fetch: {url}")
    
    # The 'await' here yields control back to the event loop
    async with session.get(url) as response:
        await response.text() # Read the content (I/O operation)
        
    end_fetch = time.time()
    print(f"[{end_fetch-start_time:.2f}s] Finished fetch: {url} (Duration: {end_fetch - start_fetch:.2f}s)")
    return response.status

async def main():
    # Use an aiohttp ClientSession for efficiency
    async with aiohttp.ClientSession() as session:
        # Create a list of all coroutine tasks
        tasks = [fetch_url(session, url) for url in urls]
        
        # 'await asyncio.gather(*tasks)' runs them all concurrently
        # It blocks until ALL tasks are complete
        statuses = await asyncio.gather(*tasks)
        return statuses

# Global start time for easy logging
start_time = time.time()

if __name__ == "__main__":
    # The entry point for asyncio, runs the event loop
    results = asyncio.run(main()) 

    end_time = time.time()
    print("\n--- Final Summary ---")
    print(f"All statuses: {results}")
    # The key observation: Total time should be close to the longest single request (1.5s), not the sum (3.2s)
    print(f"Total elapsed time: {end_time - start_time:.2f} seconds")