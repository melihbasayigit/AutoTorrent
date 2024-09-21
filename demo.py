import sys
sys.path.append("AutoTorrent")

from auto_torrent import AutoTorrent

auto_torrent = AutoTorrent()
result = auto_torrent.defaultStart(input='Lord of The Rings', qualities=["1080P","720P"])

for torrent in result:
    print(torrent)