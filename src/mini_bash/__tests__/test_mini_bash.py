import pytest
from unittest.mock import patch, MagicMock

test_dir = "/data/docker/hanoi_voice_apis--DEV/__submodules__/hanoi_utils/src/hanoi_utils/__submodules__/mini_bash"

# Import the function to test
import sys
import os
sys.path.insert(0, os.path.join(test_dir, "src"))
from mini_bash import mini_bash


class TestMiniBash:
    """Test class for mini_bash function"""

    def test_mini_bash_success(self):
        """Test successful execution of a simple bash command"""
        result = mini_bash("echo 'hello world'")
        assert isinstance(result, tuple)
        assert len(result) == 2
        stdout, stderr = result
        assert "hello world" in stdout
        assert stderr == ""

    def test_mini_bash_with_error_handling(self):
        """Test that commands with errors raise RuntimeError"""
        with pytest.raises(RuntimeError) as excinfo:
            mini_bash("ls /nonexistent/path")
        assert "cant execute" in str(excinfo.value)

    def test_mini_bash_empty_command(self):
        """Test execution of an empty command"""
        result = mini_bash("")
        assert isinstance(result, tuple)
        assert len(result) == 2
        stdout, stderr = result
        # Empty command should return empty output
        assert stdout == ""
        assert stderr == ""

    def test_mini_bash_complex_command(self):
        """Test execution of a more complex bash command"""
        result = mini_bash("echo 'test123' | grep 'test'")
        assert isinstance(result, tuple)
        assert len(result) == 2
        stdout, stderr = result
        assert "test123" in stdout
        assert stderr == ""

    def test_mini_bash_with_special_characters(self):
        """Test execution with special shell characters"""
        result = mini_bash("echo 'Hello $HOME test'")
        assert isinstance(result, tuple)
        assert len(result) == 2
        stdout, stderr = result
        assert "Hello $HOME test" in stdout
        assert stderr == ""

    def test_mini_bash_error_command(self):
        """Test error handling with a failing command"""
        # Try to execute an invalid command
        with pytest.raises(RuntimeError) as excinfo:
            mini_bash("invalid_nonexistent_command_12345")
        assert "cant execute" in str(excinfo.value)

    def test_mini_bash_stderr_output(self):
        """Test that stderr output is properly captured"""
        result = mini_bash("echo 'error message' >&2")
        stdout, stderr = result
        assert stderr == "error message\n"
        assert stdout == ""

    def test_mini_bash_multiline_output(self):
        """Test execution with multiline output"""
        result = mini_bash("echo -e 'line1\\nline2\\nline3'")
        stdout, stderr = result
        assert "line1" in stdout
        assert "line2" in stdout
        assert "line3" in stdout
        assert stderr == ""

    def test_mini_bash_exit_code_handling(self):
        """Test that non-zero exit codes raise RuntimeError"""
        with pytest.raises(RuntimeError) as excinfo:
            mini_bash("exit 1")
        assert "cant execute" in str(excinfo.value)

    def test_mini_bash_pipe_failure(self):
        """Test that pipe failures are properly handled"""
        with pytest.raises(RuntimeError) as excinfo:
            mini_bash("false | echo 'should not reach'")
        assert "cant execute" in str(excinfo.value)

    def test_mini_bash_environment_variables(self):
        """Test execution with environment variables"""
        result = mini_bash("echo $HOME")
        stdout, stderr = result
        assert stderr == ""
        # Should contain home directory path
        assert "/" in stdout

    def test_mini_bash_command_with_quotes(self):
        """Test execution with complex quoting"""
        result = mini_bash("echo \"Hello 'world' with \\\"quotes\\\"\"")
        stdout, stderr = result
        assert "Hello 'world' with \"quotes\"" in stdout
        assert stderr == ""
