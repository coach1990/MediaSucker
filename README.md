# Media Downloader from HAR File

This Python script is designed to efficiently download all media files (images, videos, etc.) listed in a **HAR file** from a website. It handles media downloads in parallel using **multithreading** to speed up the process, and avoids downloading duplicate files. The script also ensures that each downloaded file is saved with a unique name to prevent overwriting.


# How to Download a HAR File

A **HAR (HTTP Archive)** file is a detailed log of a web browser's network activity, including all HTTP requests and responses. It is commonly used for troubleshooting performance issues and capturing data from a webpage, such as media files, scripts, and other resources.

This guide will walk you through how to download a HAR file from your browser (we'll cover Chrome and Firefox).

## Step-by-Step Guide to Download a HAR File

### **Using Google Chrome:**
1. **Open Developer Tools**:
   - Press `F12` or `Ctrl + Shift + I` on your keyboard, or right-click anywhere on the page and select "Inspect".
   
2. **Go to the 'Network' Tab**:
   - Click the **"Network"** tab in the Developer Tools window.
   
3. **Record the Network Activity**:
   - Refresh the page by pressing `F5` or clicking the refresh button on your browser.
   - As the page loads, Chrome will begin recording all network requests in the "Network" tab.

4. **Save the HAR File**:
   - Once the page has fully loaded, right-click anywhere in the "Network" tab and select **"Save all as HAR with content"**.
   - Choose a location on your computer to save the HAR file. This file will contain all network requests and responses made by your browser during the page load.

---

### **Using Mozilla Firefox:**
1. **Open Developer Tools**:
   - Press `F12` or `Ctrl + Shift + I` on your keyboard, or right-click anywhere on the page and select "Inspect".
   
2. **Go to the 'Network' Tab**:
   - Click the **"Network"** tab in the Developer Tools window.

3. **Record the Network Activity**:
   - Refresh the page by pressing `F5` or clicking the refresh button on your browser.
   - Firefox will start recording all network requests made by the page as it loads.

4. **Save the HAR File**:
   - Once the page has fully loaded, click the **"Export"** button (this looks like a disk icon).
   - Select **"Save All as HAR"** from the dropdown.
   - Choose a location on your computer to save the HAR file.

---

### **Important Notes**:
- **HAR File Content**: The HAR file will contain detailed information about every HTTP request made by the browser, including images, videos, scripts, and other resources that were loaded as part of the page.
- **Privacy Considerations**: The HAR file can sometimes include sensitive information, such as authentication tokens or user data. Be cautious when sharing HAR files with others.

---

### **Where to Find the HAR File**:
After saving the HAR file, it will be in the location you specified during the saving step (typically in your "Downloads" folder or the desktop).

---

## Example of Saving a HAR File:
```
1. Press F12.
2. Go to "Network" tab.
3. Reload the page.
4. Right-click on the network tab and select "Save all as HAR with content".
5. Save the HAR file to your computer.
```

---

Now that you have your HAR file, you can proceed with running the media download script!


## Features:
- **Parallel Downloading**: Downloads media files in parallel for faster processing using `ThreadPoolExecutor`.
- **Duplicate Handling**: Avoids downloading duplicate media files.
- **Unique Filenames**: Automatically handles filename collisions by appending suffixes like `_1`, `_2`, etc.
- **Flexible Media Types**: Supports images and video formats such as `.jpg`, `.png`, `.mp4`, `.mp3`, and more.
- **User-Agent Header**: Adds a `User-Agent` header to avoid blocking by some websites.

## Requirements:
- **Python 3.x** (tested with Python 3.6+)
- **Requests library** (for HTTP requests)

You can install the required library using pip:
```
pip install requests
```

## Setup:
1. **Clone this repository** to your local machine:
   ```
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Place the HAR file** in the same directory as the script or update the `har_file` variable in the script with the correct path to your HAR file.
   - HAR file can be generated using browser developer tools (e.g., Chrome's "Network" tab and then saving the HAR).

3. **Configure the save directory** (optional):
   - The script will automatically create a folder called `downloaded_from_har` where media files will be saved. If you want to change this folder, you can update the `save_dir` variable in the script.

4. **Run the script**:
   - Once your environment is set up and the HAR file is ready, you can run the script using:
     ```
     python download_media_from_har.py
     ```

5. **Downloading in progress**:
   - The script will start downloading the media files in parallel (using multithreading) and will show the start and end messages in the terminal. For each file, it ensures no overwriting and appends a suffix if needed.

## Customization:
You can easily adjust:
- The number of threads for faster downloads by changing the `max_threads` variable.
- The types of media files to download by updating the `media_exts` list (e.g., adding `.mp4` for video).

## Example of Output:
```
⏳ Downloading 90 files using 16 threads. Please wait...

✅ Done! 90 media files downloaded successfully to: downloaded_from_har
```

## Troubleshooting:
- **Slow download speeds**: Try increasing the `max_threads` to improve speed, but note that the performance may depend on your internet connection and hardware.
- **Errors or failures in downloads**: Ensure that the URLs in your HAR file are accessible and that there are no network-related issues.

## License:
This script is Licensed under GNU. Contributions are welcome.
