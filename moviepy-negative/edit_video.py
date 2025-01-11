#!/usr/bin/env python3

from mve.src.lib.edit import edit_moviepy

from mve.src.constants.defaults import MOVIEPY_THREADS


def main():
    edit_moviepy('../videos/01.mp4', 'fish.mp4', '0', '18', MOVIEPY_THREADS)


if __name__ == "__main__":
    main()
