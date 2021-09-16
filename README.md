# viz
A Python tool to download and descramble manga from VIZ for backing up

## Disclaimer

This tool is meant to be used only for creating offline, personal, backups of content that you have bought and own. We do not endorse piracy and sharing content downloaded using this tool. The full responsibility of using this tool correctly and not misuing it for misappropriate reasons lies with the user(s).

This tool has been solely written by us, and only accesses the platform's publicly-accessible release API.

## Description

This tool can be used to download copies of Shonen Jump chapters from Viz, including both free items and those covered by the subscription. Login and password are required to download subscribtion chapters, but can be left empty otherwise.

## Installation

0. Make sure that you have Python 3 installed before installing this tool
1. Clone the tool using `git clone https://github.com/athrowaway2021/viz` or download the source code as a zip and unpack it in any location.
2. Install libraries required by the tool using `pip install -r requirements.txt`

## Usage

```
> python viz.py [manga_id]
```
```
> python viz.py 23220
23220 : Dandadan Chapter 24.0
Downloading page 027 . . .
Done! Content saved to viz_out/Dandadan Chapter 24.0
```

## Third-Party
This program uses the Python standard library and the following:
  - [Pillow](https://python-pillow.org/)
  - [requests](https://github.com/psf/requests)

See `/licenses/` for the corresponding licenses, copyright notices, and permission notices.
