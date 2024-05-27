# Overview

A mix of unit and integration tests for `mve`.  
`mve` must exist in the parent level folder:

- ie. `../mve` should be the path to access `mve`.

# Config

The default config `testing` is stored and exported as an environment variable `$CONFIG`.

# Test Structure

Each folder is a test

- automated tests have a root-level file called `run`
- manual tests have a root-level file called `start`

in videos, 4 videos are meant to be placed:

- `01..04.mp4`
- where the files are named in order of creation
- each is expected to be 1 minute and 37 seconds long

tests that need additional information have a root-level file called `info.md`
