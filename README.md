# Overview

A mix of unit and integration tests for `mve`.  
The `mve` source folder must be located in the parent: `../mve`.

To run all tests, simply run:

```sh
./run
```

.

# Test Structure

Each folder is a test

- automated tests have a root-level file called `run`
- manual tests have a root-level file called `start`

# Environment

The script `setup-env` must be sourced by all test scripts, in order to load
necessary environment variables,
