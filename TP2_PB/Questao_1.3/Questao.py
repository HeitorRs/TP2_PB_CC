import os
import asyncio
from PIL import Image, ImageFilter
import time
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor

async def process_image(image_path, output_dir):
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, process_image_sync, image_path, output_dir)


def process_image_sync(image_path, output_dir):
    img = Image.open(image_path)
    img = img.filter(ImageFilter.EMBOSS)
    img.save(os.path.join(output_dir, os.path.basename(image_path)))


async def main_image_processing(input_dir, output_dir, num_threads):
    os.makedirs(output_dir, exist_ok=True)
    images = [
        os.path.join(input_dir, img)
        for img in os.listdir(input_dir)
        if img.endswith(".jpg")
    ]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        loop = asyncio.get_running_loop()
        tasks = [
            loop.run_in_executor(executor, process_image_sync, img, output_dir)
            for img in images
        ]
        await asyncio.gather(*tasks)


def benchmark(input_dir, output_dir, thread_counts):
    times = []
    for num_threads in thread_counts:
        start_time = time.time()
        asyncio.run(main_image_processing(input_dir, output_dir, num_threads))
        end_time = time.time()
        times.append(end_time - start_time)
        print(f"Threads: {num_threads}, Tempo: {end_time - start_time:.2f}s")
    return times


def plot_results(thread_counts, times):
    plt.figure(figsize=(10, 6))
    plt.plot(thread_counts, times, marker="o", linestyle="-")
    plt.xlabel("Número de Threads")
    plt.ylabel("Tempo (segundos)")
    plt.title("Desempenho: Número de Threads vs Tempo")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    input_dir = "Questao_1.3/input_images"
    output_dir = "Questao_1.3/output_images"
    thread_counts = [1, 2, 4, 8, 16]

    times = benchmark(input_dir, output_dir, thread_counts)
    plot_results(thread_counts, times)
