#!/usr/bin/env python3

r = '\033[1;0m' # reset

colours = {
    'orange attempt': '\033[2;103m', # bright yellow background
    'yellow text': '\033[1;103m', # bright yellow background pickle colour text
    'after white': '\033[1;38m'
}

def attempt(key):
    print(f'attempt {key}: {colours[key]}text{r} end')

for c in colours:
    attempt(c)