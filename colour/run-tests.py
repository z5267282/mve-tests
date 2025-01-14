import sys

import mve.src.constants.colours as colours

import mve.src.helpers.colouring as colouring

colours = [
    colours.BLACK,
    colours.RED,
    colours.GREEN,
    colours.YELLOW,
    colours.BLUE,
    colours.PURPLE,
    colours.CYAN,
    colours.WHITE,
]

colour_names = 'black red green yellow blue purple cyan white'

for c, n in zip(colours, colour_names.split()):
    verify = input(
        f"enter y if this {colouring.colour_format(c, 'text', False)} is in {n}: ")
    if not verify == 'y':
        print(f'failed test for colour {n}', file=sys.stderr)
        sys.exit(1)

print('\npassed all colour tests!')
