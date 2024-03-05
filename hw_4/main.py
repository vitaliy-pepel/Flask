import asyncio
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import aiohttp
from PIL import Image
from flask import Flask, request

app = Flask(__name__)


def download_image(url, requests=None):
    start_time = time.time()
    image_name = url.split('/')[-1]
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return
    with open(image_name, 'wb') as file:
        file.write(response.content)
    end_time = time.time()
    print(f"Image {image_name} downloaded in {end_time - start_time} seconds")


def download_images_threads(urls):
    start_time = time.time()
    with ThreadPoolExecutor() as executor:
        executor.map(download_image, urls)
    end_time = time.time()
    print(f"All images downloaded in {end_time - start_time} seconds")


def download_images_processes(urls):
    start_time = time.time()
    with ProcessPoolExecutor() as executor:
        executor.map(download_image, urls)
    end_time = time.time()
    print(f"All images downloaded in {end_time - start_time} seconds")


async def download_image_async(session, url):
    start_time = time.time()
    image_name = url.split('/')[-1]
    async with session.get(url) as response:
        if response.status != 200:
            print(f"Error: Image {image_name} not found")
            return
        with open(image_name, 'wb') as file:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                file.write(chunk)
    end_time = time.time()
    print(f"Image {image_name} downloaded in {end_time - start_time} seconds")


async def download_images_async(urls):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(download_image_async(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"All images downloaded in {end_time - start_time} seconds")


@app.route('/download', methods=['POST'])
def download():
    urls = request.json['urls']
    asyncio.run(download_images_async(urls))
    return "Images downloaded"


if __name__ == '__main__':
    app.run(debug=True)


