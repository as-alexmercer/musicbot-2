import os
import pytest
from click_skeleton.testing import run_cli
from musicbot.cli import main_cli
from . import fixtures


@pytest.mark.runner_setup(mix_stderr=False)
def test_youtube_search(cli_runner):
    run_cli(cli_runner, main_cli, [
        '--quiet',
        'youtube', 'search',
        'buckethead', 'welcome to bucketheadland',
    ])


@pytest.mark.runner_setup(mix_stderr=False)
def test_youtube_download(cli_runner):
    try:
        run_cli(cli_runner, main_cli, [
            '--quiet',
            'youtube', 'download',
            'buckethead', 'welcome to bucketheadland',
            '--path', 'test.mp3',
        ])
    finally:
        try:
            os.remove('test.mp3')
        except OSError:
            pass


@pytest.mark.runner_setup(mix_stderr=False)
def test_youtube_fingerprint(cli_runner):
    run_cli(cli_runner, main_cli, [
        '--quiet',
        'youtube', 'fingerprint',
        fixtures.youtube_url,
    ])


@pytest.mark.runner_setup(mix_stderr=False)
def test_youtube_find(cli_runner):
    run_cli(cli_runner, main_cli, [
        '--quiet',
        'youtube', 'find',
        fixtures.one_mp3,
    ])
