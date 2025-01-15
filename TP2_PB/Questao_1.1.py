import asyncio
import aiohttp
import time
import matplotlib.pyplot as plt

async def download_url(session, url):
    async with session.get(url) as response:
        content = await response.text()

async def download_urls_concurrent(urls, concurrency_level):
    connector = aiohttp.TCPConnector(limit_per_host=concurrency_level)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for i in range(0, len(urls), concurrency_level):
            batch = urls[i:i + concurrency_level]
            tasks.append(asyncio.gather(*(download_url(session, url) for url in batch)))
        await asyncio.gather(*tasks)

def measure_download_time(urls, concurrency_level):
    start_time = time.time()
    asyncio.run(download_urls_concurrent(urls, concurrency_level))
    return time.time() - start_time

def main():
    urls = [
        "https://example.com", 
        "https://httpbin.org/get", 
        "https://jsonplaceholder.typicode.com/posts", 
        "https://reqres.in/api/users",
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/albums",
        "https://jsonplaceholder.typicode.com/photos",
        "https://jsonplaceholder.typicode.com/todos",
        "https://jsonplaceholder.typicode.com/users",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/3",
        "https://httpbin.org/delay/4",
        "https://httpbin.org/delay/5",
        "https://httpbin.org/delay/6",
        "https://httpbin.org/delay/7",
        "https://httpbin.org/delay/8"
    ]
    
    concurrency_levels = [1, 2, 4, 8, 16, 32, 64]
    times = []

    for concurrency_level in concurrency_levels:
        print(f"Medindo tempo para {concurrency_level} downloads concorrentes...")
        time_taken = measure_download_time(urls, concurrency_level)
        times.append(time_taken)
        print(f"Tempo gasto com {concurrency_level} downloads concorrentes: {time_taken:.2f} segundos")
    
    plt.plot(concurrency_levels, times, marker='o')
    plt.xlabel('Numero de Downloads Concorrentes')
    plt.ylabel('Tempo (segundos)')
    plt.title('Numero de Threads vs Tempo para Download URLs')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()



