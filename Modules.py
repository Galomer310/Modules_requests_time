import requests
import time

def measure_load_time(url):
    start_time = time.time()
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    
    end_time = time.time()
    load_time = end_time - start_time
    
    return load_time

urls = ["https://www.google.com", "https://www.ynet.co.il", "https://www.imdb.com"]

for url in urls:
    print(f"Load time for {url}: {measure_load_time(url)} seconds")
