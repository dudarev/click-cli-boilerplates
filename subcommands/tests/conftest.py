import pytest

from click.testing import CliRunner
from pathlib import Path


@pytest.fixture
def cli_runner_and_dir(tmp_path) -> tuple[CliRunner, Path]:
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=tmp_path) as cli_runner_dir:
        yield runner, Path(cli_runner_dir)
