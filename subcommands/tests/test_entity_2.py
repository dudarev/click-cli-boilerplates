from src.entity_2 import hello


def test_hello(cli_runner_and_dir):
    runner, _ = cli_runner_and_dir
    result = runner.invoke(hello, [])
    assert result.exit_code == 0
    assert result.output == "Hello from entity 2\n"
