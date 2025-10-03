# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python package called `mini_bash` that provides a simple interface for running bash commands from Python. The main implementation is contained in a single file `mini_bash.py` which exports one function: `mini_bash()`.

## Key Files and Structure

- `README.md`: Documentation for users, including installation and usage instructions
- `pyproject.toml`: Project configuration using Poetry packaging system
- `src/mini_bash.py`: Main implementation file containing the `mini_bash()` function
- `src/__init__.py`: Empty init file (package marker)
- `src/mini_bash/__tests__/test_mini_bash.py`: Unit tests for the mini_bash function

## Core Functionality

- Main function: `mini_bash(cmd, executable="/bin/bash", shell=True, capture_output=True, text=True)`
- Executes bash commands with enhanced error handling
- Uses `subprocess.run()` with strict error checking
- Raises `RuntimeError` on command failure with detailed error information
- Sets `set -Eeuo pipefail` for better shell error handling

## Development Commands

### Setup and Installation
```bash
# Install in development mode
pip install -e .

# Install testing dependencies
pip install -r requirements.testing.txt
```

### Testing
```bash
# Run all tests
pytest src/hanoi_utils/__submodules__/mini_bash/src/mini_bash/__tests__

# Run a specific test file
pytest src/hanoi_utils/__submodules__/mini_bash/src/mini_bash/__tests__/test_mini_bash.py

# Run a specific test function
pytest src/hanoi_utils/__submodules__/mini_bash/src/mini_bash/__tests__/test_mini_bash.py::test_mini_bash_success
```

### Build Commands
The project uses Poetry as the build backend:

```bash
# Build distribution
poetry build

# Install in development mode
poetry install
```

## Common Development Tasks

1. Adding new test cases for edge cases in bash command execution
2. Enhancing error reporting with more detailed information
3. Improving shell safety features
4. Adding support for additional subprocess options