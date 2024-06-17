from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
import os
import argparse


def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(outpt_path=save_path)
    except Exception as e:
        print(e)


def parse_url() -> str:
    parser = argparse.ArgumentParser("Download a YouTube video")
    parser.add_argument("url", help="URL of the YouTube video to be downloaded")
    args = parser.parse_args()
    return args.url


def main():
    url = parse_url()

    current_dir = os.path.dirname(os.path.realpath(__file__))
    save_path = os.path.join(current_dir, "..", "video_downloads")

    download_video(url, save_path)


if __name__ == "__main__":
    main()
