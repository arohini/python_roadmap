import threading
import time
import requests

# Shared resource and lock
SHARED_RESULTS = []
results_lock = threading.Lock()

def fetch_url(url):
    """Simulates fetching a URL and processing a result."""
    try:
        # Simulate network wait time
        response = requests.get(url, timeout=3)
        result_text = f"URL: {url}, Status: {response.status_code}"

        # CRITICAL SECTION: Use the lock to protect SHARED_RESULTS
        with results_lock:
            SHARED_RESULTS.append(result_text)
            print(f"--> Appended result for {url}")
            
    except requests.exceptions.RequestException as e:
        # Unsafe for simplicity: This still might interfere with other print calls
        print(f"Error fetching {url}: {e}")

# List of URLs to fetch concurrently
urls = [
    'https://www.google.com',
    'https://www.python.org',
    'https://www.bing.com',
    'https://www.apple.com'
]

threads = []
start_time = time.time()


# Create and start threads
for url in urls:
    t = threading.Thread(target=fetch_url, args=(url,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()


# for url in urls:
#     fetch_url(url=url)

end_time = time.time()

print("\n--- Results ---")
print(f"Total time taken: {end_time - start_time:.2f} seconds")
print(f"Total results collected: {len(SHARED_RESULTS)}")
# The Lock ensures no race conditions when modifying SHARED_RESULTS