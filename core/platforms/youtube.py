from pytube import YouTube

def get_m3u8_link(video_url):
    yt = YouTube(video_url)
    stream = yt.streams.filter(progressive=False, file_extension='m3u8').first()
    if stream:
        return stream.url
    else:
        raise ValueError("No m3u8 stream found for the video.")

if __name__ == "__main__":
    import sys
    video_url = sys.argv[1]
    try:
        m3u8_link = get_m3u8_link(video_url)
        print(m3u8_link)
    except Exception as e:
        print(f"Error: {e}")
