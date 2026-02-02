# mini_bash

> **Summary**: A lightweight Python package for executing bash commands programmatically with automatic error handling. Raises an exception if the shell command returns a non-zero exit code.

## Installation

You can install mini_bash using pip:

```bash
pip install mini_bash
```

## Usage

```python
from mini_bash import mini_bash

# Execute a command and capture output
std_out_str, std_err_str = mini_bash('ls -ltr')

# The function returns a tuple of (stdout, stderr)
print(f"Output: {std_out_str}")
print(f"Errors: {std_err_str}")
```

### Error Handling

If the command exits with a non-zero return code, a `subprocess.CalledProcessError` is raised:

```python
from mini_bash import mini_bash

try:
    mini_bash('exit 1')
except Exception as e:
    print(f"Command failed: {e}")
```

## Contribution & License

If you have any suggestions, improvements, or issues regarding **mini_bash**, feel free to [open an issue](https://github.com/lamnt45/mini_bash/issues) or submit a pull request on GitHub.

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
