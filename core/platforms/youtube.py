import subprocess
import sys

def download_m3u8(video_url, output_path):
    try:
        command = [
            "yt-dlp",
            "--get-url",
            "--format", "best",
            video_url
        ]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        with open(output_path, 'w') as f:
            f.write(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    video_url = sys.argv[1]
    output_path = sys.argv[2]
    download_m3u8(video_url, output_path)

