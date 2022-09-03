import sys

import colour

colours = [
    colour.BLACK,
    colour.RED,
    colour.GREEN,
    colour.YELLOW,
    colour.BLUE,
    colour.PURPLE,
    colour.CYAN,
    colour.WHITE,
]

colour_names = 'black red green yellow blue purple cyan white'

for c, n in zip(colours, colour_names.split()):
    verify = input(f"enter y if this {c}text{colour.RESET} is in {n}: ")
    if not verify == 'y':
        print(f'failed test for colour {n}', file=sys.stderr)
        sys.exit(1)

print('\npassed all colour tests!')