import yt_dlp

def download_playlist(playlist_url):
    try:
        options = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'merge_output_format': None,  # Skip merging
            'noplaylist': False,
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([playlist_url])

        print("Download complete!")
    except yt_dlp.DownloadError as e:
        for err in e.exc_info:
            if isinstance(err, yt_dlp.utils.ExtractorError) and 'unavailable' in str(err):
                print("Skipped unavailable audio.")
            else:
                print(f"An error occurred: {err}")
                continue

# Replace 'YOUR_PLAYLIST_URL' with the actual URL of the playlist you want to download
playlist_url = input("Enter playlist url: ")
download_playlist(playlist_url)
