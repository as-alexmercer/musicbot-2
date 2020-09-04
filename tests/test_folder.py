import pytest
from click_skeleton import run_cli
from musicbot.cli import cli
from . import fixtures


@pytest.mark.runner_setup(mix_stderr=False)
def test_folder_find(cli_runner):
    musics = run_cli(cli_runner, cli, ['folder', 'find', *fixtures.folders])
    assert len(musics.split("\n")) == 5


@pytest.mark.runner_setup(mix_stderr=False)
def test_folder_flac2mp3(cli_runner):
    run_cli(cli_runner, cli, ['folder', 'flac2mp3', '--dry', *fixtures.folders])


@pytest.mark.runner_setup(mix_stderr=False)
def test_folder_tracks(cli_runner):
    run_cli(cli_runner, cli, ['folder', 'tracks', *fixtures.folders])


@pytest.mark.runner_setup(mix_stderr=False)
def test_folder_check_consistency(cli_runner):
    run_cli(cli_runner, cli, ['folder', 'consistency', *fixtures.folders])
