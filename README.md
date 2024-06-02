# Fix New Config System

Must fix:

1. `PATH` variable
2. Test working
3. Clean old structure

| test                  | fixed |
| --------------------- | ----- |
| colour                | Start |
| decimal               | Yes   |
| duration-ffmpeg-probe | Start |
| edit-integration      | Yes   |
| editing               | Yes   |
| empty-queue           | Yes   |
| error-integration     | Yes   |
| ffmpeg-integration    | Yes   |
| ffmpeg-unit           | Start |
| misc                  | Yes   |
| moment-good           | Yes   |
| moviepy-negative      | Start |
| name-existence        | Yes   |
| no-destination        | Yes   |
| no-queue              | Yes   |
| no-renames            | Yes   |
| prompt-align          | Start |
| sandbox               | Start |
| test-edit-exists      | Yes   |
| timestamp             | Yes   |

# Overview

A mix of unit and integration tests for `mve`.  
`mve` must exist in the parent level folder:

- ie. `../mve` should be the path to access `mve`.

# Environment Configuration

The script `setup-env` should be sourced all tests.  
This includes the config generation.  
The following config options can be set using `JSON` as environmnet variables.  
All other options are set according to the default configuration.

- `RECENT`

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
