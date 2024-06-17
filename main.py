from pytube import YouTube
import os
import argparse


def download_video(url, save_path):
    try:
        yt = YouTube(url)
        print(f"Downloading video: {yt.title}")
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        print(f"Selected stream: {highest_res_stream}")
        highest_res_stream.download(output_path=save_path)
        print("Downloaded successfully")
    except Exception as e:
        print(f"Error: {e}")


def parse_url() -> str:
    parser = argparse.ArgumentParser(description="Download a YouTube video")
    parser.add_argument("url", help="URL of the YouTube video to be downloaded")
    args = parser.parse_args()
    return args.url


def main():
    url = parse_url()
    print(f"URL to download: {url}")

    current_dir = os.path.dirname(os.path.realpath(__file__))
    save_path = os.path.join(current_dir, "video_downloads")
    print(f"Save path: {save_path}")

    # Ensure the save path directory exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)
        print(f"Created directory: {save_path}")

    download_video(url, save_path)


if __name__ == "__main__":
    main()
