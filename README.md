# Overview

A mix of unit and integration tests for `mve`.  
The `mve` source folder must be located in the parent: `../mve`.

To run all tests, simply run:

```sh
./run
```

.

## Options

Usage:

```
run [--clean] [--debug] [--name] <name1,name2,...> [--help]
```

.

| Flag                       | Description                                                      |
| -------------------------- | ---------------------------------------------------------------- |
| `--clean`                  | Delete all folders generated after testing is complete.          |
| `--debug`                  | Show all output during testing.                                  |
| `--name` <name1,name2,...> | Only run tests that contain either `name1` or `name2` or `...` . |

# Test Structure

Each folder except `helpers` is a test.

- Automated tests have a root-level file called `run`.
- Manual tests have a root-level file called `start`.

# Environment

The script `setup-env` must be sourced by all test scripts, in order to load
necessary environment variables,
