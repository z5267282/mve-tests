'''Generate all necessary videos for testing. A folder videos is created in
the root, with four copies of a generated video, 01..04.mp4 .
This script is meant to be run inside of make-videos, as it relies on
environment variables that need to be sourced.'''

import json

import os

import cv2
import numpy as np

RGB = 'rgb.json'


def main():
    colours = load_colours()
    fps = int(os.environ["FPS"])

    width = int(os.environ["HEIGHT"])
    height = int(os.environ["HEIGHT"])

    num_seconds = int(os.environ["LEN"])
    output = os.environ["OUTPUT"]

    generate_video(colours, fps, width, height, output, num_seconds)


def load_colours() -> list[tuple[int, int, int]]:
    with open(RGB) as f:
        colours = json.load(f)
    return colours


def generate_video(colours: list[tuple[int, int, int]], fps: int, width: int,
                   height: int, output: str, num_seconds: int):
    # fourcc is an int code that translates to a filetype
    fourcc = cv2.VideoWriter.fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output, fourcc, fps, (width, height))

    # Iterate over the RGB values and create frames
    for i, rgb in enumerate(colours[:num_seconds]):
        print(f'colour {i:2d} loaded')
        # the tuple is (height, width, num. colour values: 3 in "RGB")
        frame = np.zeros((height, width, 3), np.uint8)
        frame[:, :, :] = rgb

        # write all fps frames to the video
        for _ in range(fps):
            video_writer.write(frame)

    # Release the video writer
    video_writer.release()

    print(f'successfully created video {output}')


if __name__ == '__main__':
    main()
