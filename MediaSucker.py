import json
import os
import requests
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

# Path to your HAR file
har_file = 'app.leonardo.ai.har'

# Folder to save media files
save_dir = 'downloaded_from_har'
os.makedirs(save_dir, exist_ok=True)

# File types to download
media_exts = ['.jpg', '.jpeg', '.png', '.webp', '.gif', '.mp4', '.webm', '.ogg', '.mp3']

# Load HAR data
with open(har_file, 'r', encoding='utf-8') as f:
    har_data = json.load(f)

# Collect unique media URLs
entries = har_data['log']['entries']
seen_urls = set()
media_urls = []

for entry in entries:
    url = entry['request']['url']
    parsed = urlparse(url)
    ext = os.path.splitext(parsed.path)[-1].lower()
    if ext in media_exts and url not in seen_urls:
        media_urls.append(url)
        seen_urls.add(url)

print(f"\n⏳ Downloading {len(media_urls)} media files using threads. Please wait...\n")

# Keep track of used filenames
used_filenames = set()

def download_media(url, index):
    try:
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path) or f"file_{index}"
        base, ext = os.path.splitext(filename)
        if ext not in media_exts:
            ext = '.bin'
        filename = f"{base}{ext}"

        # Make filename unique
        count = 1
        while filename in used_filenames:
            filename = f"{base}_{count}{ext}"
            count += 1
        used_filenames.add(filename)

        # Perform download
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, stream=True, timeout=15, headers=headers)
        response.raise_for_status()

        filepath = os.path.join(save_dir, filename)
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        return True
    except:
        return False

# Download with threads (adjust max_workers if needed)
max_threads = 16
success_count = 0

with ThreadPoolExecutor(max_workers=max_threads) as executor:
    futures = [executor.submit(download_media, url, i) for i, url in enumerate(media_urls)]
    for future in as_completed(futures):
        if future.result():
            success_count += 1

print(f"✅ Done! {success_count} media files downloaded successfully to: {save_dir}")
