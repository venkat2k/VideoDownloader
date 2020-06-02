## Description
VideoDownloader is a Python based GUI application that is used to download videos from YouTube. 

## Features
- Enter a SearchText and the application will automatically find an appropriate video and download it.
- Enter a YouTube URL directly to download a specific video.
- Download in MP4 or MP3 format.
- Use the application on any Windows PC with the exe file.

## Getting Started
- Clone the repository and install the required packages using pip.
 ```pip install -r requirements.txt```
- Run the downloader.py file.
- Alternatively, you can copy the VideoDownloader folder anywhere on your computer and execute the application using the downloader.exe file. There is no need for any packages or Python for this to work. Remember to copy the entire folder.

## How it works?
- We append the search text to the YouTube URL and use WebScraping to fetch the URL of the first video from the results.
- Once we have the URL, the video is downloaded using pytube library. 
- The front-end is handled by PyQt5

## Note
- This was not created for commercial use, as it could be used to download copyrighted content. It is just a fun project.
