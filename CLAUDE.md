# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

mini_bash is a simple Python package that provides a convenient wrapper for running bash commands with proper error handling. The package is built using Poetry and follows standard Python packaging conventions.

## Development Commands

### Building and Publishing
- Build package: `poetry build`
- Publish to PyPI: `poetry publish`
- Install dependencies: `poetry install`

### Testing
Currently there are no automated tests in the repository. The main functionality is contained in a single file (`src/mini_bash.py`) and can be tested manually by importing and using the `mini_bash` function.

## Code Architecture

### Core Function
- **Location**: `src/mini_bash.py:12`
- **Function**: `mini_bash(cmd, executable="/bin/bash", shell=True, capture_output=True, text=True)`
- **Purpose**: Wraps subprocess.run with bash-specific defaults and error handling
- **Key Features**:
  - Automatically prepends `set -Eeuo pipefail` for safer bash execution
  - Captures stdout and stderr by default
  - Raises RuntimeError with command and stderr on non-zero exit codes
  - Returns tuple of (stdout, stderr)

### Package Structure
- Single module package with minimal dependencies
- Uses Poetry for dependency management and packaging
- Follows standard Python package structure with `src/` layout

## Development Notes

- The package has no external dependencies beyond Python standard library
- Uses Apache 2.0 license (specified in pyproject.toml, MIT in README)
- Version management handled through Poetry
- Published on PyPI as `mini_bash`

## Common Tasks

When adding new features or making changes:
1. Update version in `pyproject.toml`
2. Test the `mini_bash` function with various bash commands
3. Build and test locally before publishing
4. Update README.md if functionality changes