#!/usr/bin/env python3

import moviepy.editor as mvp

import config as cfg
import video_editing as vde

def edit():
    with mvp.VideoFileClip('../videos/01.mp4') as file:
        clip = file.subclip(t_end=-18)
        clip.write_videofile(
            'fish.mp4',
            threads=cfg.NUM_THREADS,
            fps=vde.FRAMES,
            codec=vde.VCODEC,
            preset=vde.COMPRESSION,
            audio_codec=vde.ACODEC
        )

def main():
    edit()

if __name__ == "__main__":
    main()
