# Fix New Config System

| test                  | fixed |
| --------------------- | ----- |
| colour                |       |
| decimal               |       |
| duration-ffmpeg-probe |       |
| edit-integration      | Yes   |
| editing               |       |
| empty-queue           | Yes   |
| error-integration     |       |
| ffmpeg-integration    |       |
| ffmpeg-unit           |       |
| misc                  |       |
| moment-good           |       |
| moviepy-negative      |       |
| name-existence        |       |
| no-destination        |       |
| no-queue              |       |
| no-renames            |       |
| prompt-align          |       |
| sandbox               |       |
| test-edit-exists      |       |
| timestamp             |       |
| videos                |       |

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

# Sample Videos

In `videos`, 4 videos are meant to be placed:

- `01..04.mp4`
- where the files are named in order of creation
- each is expected to be 1 minute and 37 seconds long

# Intellisense

Intellisense path alterations have been done stored in `.vscode`.
