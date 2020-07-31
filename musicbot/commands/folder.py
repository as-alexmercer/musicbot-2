import logging
import json
import concurrent.futures as cf
import click
from prettytable import PrettyTable
from musicbot import helpers, lib
from musicbot.config import config
from musicbot.music.file import File, folder_option, checks_options

logger = logging.getLogger(__name__)


@click.group(help='Manage folders', cls=helpers.GroupWithHelp)
def cli():
    pass


@cli.command(help='List tracks')
@helpers.add_options(
    helpers.folders_argument +
    helpers.output_option
)
def tracks(folders, output):
    tracks = helpers.genfiles(folders)
    if output == 'json':
        tracks_dict = [{'title': t.title, 'artist': t.artist, 'album': t.album} for t in tracks]
        print(json.dumps(tracks_dict))
    elif output == 'table':
        pt = PrettyTable()
        pt.field_names = ["Track", "Title", "Artist", "Album"]
        for t in tracks:
            pt.add_row([t.number, t.title, t.artist, t.album])
        print(pt)
    else:
        raise NotImplementedError


@cli.command(help='Convert all files in folders to mp3')
@helpers.add_options(
    folder_option +
    helpers.folders_argument +
    helpers.concurrency_options +
    helpers.dry_option
)
def flac2mp3(folders, folder, concurrency, dry):
    flac_files = list(lib.find_files(folders, ['flac']))
    if not flac_files:
        logger.warning(f"No flac files detected in {folders}")
        return

    with config.tqdm(total=len(flac_files), leave=True, desc='Converting musics') as pbar:
        with cf.ThreadPoolExecutor(max_workers=concurrency) as executor:
            def convert(flac_path):
                f = File(flac_path)
                f.to_mp3(folder, dry)
                pbar.update(1)
            executor.shutdown = lambda wait: None
            futures = [executor.submit(convert, flac_path[1]) for flac_path in flac_files]
            cf.wait(futures)


@cli.command(help='Check music files consistency')
@helpers.add_options(
    helpers.folders_argument +
    helpers.dry_option +
    checks_options
)
def check_consistency(folders, **kwargs):
    musics = helpers.genfiles(folders)
    pt = PrettyTable()
    pt.field_names = ["Folder", "Path", "Inconsistencies"]
    for m in musics:
        try:
            inconsistencies = m.check_consistency(**kwargs)
            if inconsistencies:
                pt.add_row([m.folder, m.path, ', '.join(inconsistencies)])
        except OSError:
            pt.add_row([m.path, "Could not open file"])
    print(pt)
