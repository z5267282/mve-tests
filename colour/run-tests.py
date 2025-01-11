import sys

import mve.src.constants.colours as clr

import mve.src.helpers.colouring as colouring

colours = [
    clr.BLACK,
    clr.RED,
    clr.GREEN,
    clr.YELLOW,
    clr.BLUE,
    clr.PURPLE,
    clr.CYAN,
    clr.WHITE,
]

colour_names = 'black red green yellow blue purple cyan white'

for c, n in zip(colours, colour_names.split()):
    verify = input(
        f"enter y if this {colouring.colour_format(c, 'text', False)} is in {n}: ")
    if not verify == 'y':
        print(f'failed test for colour {n}', file=sys.stderr)
        sys.exit(1)

print('\npassed all colour tests!')
