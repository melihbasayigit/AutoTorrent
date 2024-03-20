# Auto Torrent

![Logo](#) Coming Soon


Auto Torrent is a torrent scrapper and downloader.

## Requirments

- Python
- Python-Dotenv
- Qbittorrent Web UI

## Installation

If you have already install all requirments above,

Copy the AutoTorrent folder and past it in your project. Import and Use it.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file (in torrent module)

`QB_USERNAME`

`QB_PASSWORD`

`QB_WEB_UI`

**NOTE** and also you need to add your paths to category_type.py correctly. I will fix that soon. 

## Usage

In python:

```python
from AutoTorrent import AutoTorrent
from AutoTorrent.auto_torrent import AutoTorrent
from AutoTorrent.torrent.torrent_manager import TorrentManager
from AutoTorrent.torrent.enum.category_type import CategoryType

# Search Movie in YTS
autoTorrent = AutoTorrent()
movieList = autoTorrent.start('MOVIE NAME', allowed_qualities=[])

# Add a Torrent to Qbittorrent Web UI
manager = TorrentManager()
theLastTorrentName = manager.insert_torrent(magnet_link='Magnet Link',category_type=CategoryType.MOVIE)
```

Example of .env file:
```env
QB_USERNAME=admin
QB_PASSWORD=123456
QB_WEB_UI=http://127.0.0.1:9000
```

## Documentation

[Documentation](#) Coming Soon

## FAQ

#### EnvError: Please provide QB_USERNAME, QB_PASSWORD, and QB_WEB_UI in the .env file.

You need to check your .env file is correct. There is an example [.env](#usage) file

#### Where is my downloaded files.

I will fix savepath soon. You find all paths in category_type.py

## Appendix

Install dotenv

```bash
pip install python-dotenv
```

## Related

[AutoTorrentDjango](#) Coming Soon
