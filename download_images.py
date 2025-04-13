#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import os

# Configuration
server_url = "http://10.0.0.108:8000"  # Replace with your Windows server IP and port
output_dir = "./downloaded_images"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

def download_image(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        file_name = image_url.split("/")[-1]
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Downloaded: {file_name}")
    else:
        print(f"Failed to download: {image_url}")

# Get the HTML page with the list of images
response = requests.get(server_url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.find_all("a"):
        href = link.get("href")
        if href.lower().endswith((".jpg", ".jpeg", ".png")):
            image_url = f"{server_url}/{href}"
            download_image(image_url)
else:
    print("Failed to connect to the server.")

