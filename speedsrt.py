"""
Subtitle Speed Adjuster

Command-line tool for adjusting the speed of subtitles in a SubRip (SRT) file.

Usage:
    python script.py SRC [-s SPEED] [DST]

Arguments:
    SRC (str): Path to the source SubRip (SRT) file.
    DST (str, optional): Path to the destination SubRip (SRT) file.
        If not provided, the modified subtitles will be printed to the console.

Options:
    -s, --speed SPEED (float): Speed factor to adjust subtitle timing (default: 1.0).

Examples:
    1. Adjust subtitle speed by doubling it:
        ```
        python script.py input.srt -s 2.0
        ```

Description:
    This tool reads SubRip (SRT) formatted subtitles from the source file (SRC),
    adjusts the timing of each subtitle line based on the specified speed factor,
    and optionally writes the modified subtitles to a destination file (DST).

    The speed factor determines how much to scale the timing of each subtitle.
    For example, a speed factor of 2.0 doubles the speed, while a factor of 0.5 halves it.

    If no destination file is provided, the modified subtitles will be printed to the console.
"""


import logging
from pathlib import Path

import srt
import click
from rich.logging import RichHandler


logging.basicConfig(level=logging.DEBUG, format="%(message)s", handlers=(RichHandler(), ))
log = logging.getLogger()


ENCODING = "UTF-8"
CONTEXT_SETTINGS = {"help_option_names": ["--help", "-h"]}


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("src", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True))
@click.argument("dst", required=False, type=click.Path(exists=False, file_okay=True, dir_okay=False, readable=True))
@click.option("-s", "--speed", "speed", type=click.FloatRange(0.1, 10.0), default=1.0, prompt=True)
def cli(src: str, dst: str, speed: float):
    """Command line interface."""
    src: Path = Path(src)
    dst: Path | None = Path(dst) if dst else None
    log.debug("Parameter: src = %r.", src)
    log.debug("Parameter: dst = %r.", dst)
    log.debug("Parameter: speed = %r.", speed)

    subtitle_generator = list(srt.parse(src.read_text(encoding=ENCODING)))
    for line in subtitle_generator:
        line.start /= speed
        line.end /= speed

    doc = "".join(line.to_srt() for line in subtitle_generator)

    if dst:
        dst.write_text(doc, encoding=ENCODING)
    else:
        print(doc)


if __name__ == "__main__":
    import sys
    if len(sys.argv) <= 1:
        cli.main(["--help"])
    cli.main()
