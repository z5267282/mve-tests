import json

COLOURS = 'all-colours.json'
OUTPUT = 'rbg.json'

with open(COLOURS, 'r') as f:
    data = json.load(f)


def hex_to_rgb(hex):
    '''Taken from: https://www.30secondsofcode.org/python/s/hex-to-rgb/'''
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))


with open(OUTPUT, 'w') as f:
    # remove leading hash in hex values
    rgbs = [hex_to_rgb(hex[1:]) for hex in data["hex"]]
    json.dump(rgbs, f, indent=4)
