from click.testing import CliRunner

from src.entity_1 import hello, hey


def test_hello(cli_runner_and_dir):
    runner, _ = cli_runner_and_dir
    result = runner.invoke(hello, [])
    assert result.exit_code == 0
    assert result.output == "Hello from entity 1\n"


def test_hey():
    runner = CliRunner()
    result = runner.invoke(hey, [])
    assert result.exit_code == 0
    assert result.output == "Hey from entity 1\n"
