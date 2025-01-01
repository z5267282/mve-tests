import json

import cv2
import numpy as np

HEIGHT = 1080
WIDTH = 1920

FPS = 60

# expected 1:37 video for testing
LEN = 60 + 37

with open('rgb.json') as f:
    colours = json.load(f)

# fourcc is an int code that translates to a filetype
fourcc = cv2.VideoWriter.fourcc(*'mp4v')
video_writer = cv2.VideoWriter('generated.mp4', fourcc, FPS, (1920, 1080))

# Iterate over the RGB values and create frames
for rgb in colours:
    # the tuple is (height, width, num. colour values: 3 in "RGB")
    frame = np.zeros((1080, 1920, 3), np.uint8)
    frame[:, :, :] = rgb

    # write all FPS frames to the video
    for _ in range(FPS):
        video_writer.write(frame)

# Release the video writer
video_writer.release()
