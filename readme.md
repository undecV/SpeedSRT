# SpeedSRT

SpeedSRT is a command-line tool for adjusting the speed of subtitles in a SubRip (SRT) file.
This tool allows users to modify the timing of subtitles based on a specified speed factor.

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python script.py SRC [DST] [-s SPEED]
```

### Arguments

- `SRC` (str): Path to the source SubRip (SRT) file.
- `DST` (str, optional): Path to the destination SubRip (SRT) file.
  If not provided, the modified subtitles will be printed to the console.

### Options

- `-s, --speed SPEED` (float): Speed factor to adjust subtitle timing (default: 1.0).

### Examples

1. Adjust subtitle speed by doubling it:

```bash
python script.py input.srt -s 2.0
```

## Description

This tool reads SubRip (SRT) formatted subtitles from the source file (`SRC`),
adjusts the timing of each subtitle line based on the specified speed factor,
and optionally writes the modified subtitles to a destination file (`DST`).

The speed factor determines how much to scale the timing of each subtitle.
For example, a speed factor of 2.0 doubles the speed, while a factor of 0.5 halves it.

If no destination file is provided, the modified subtitles will be printed to the console.
