from typing import List
from torrent.torrent_manager import TorrentManager, CategoryType
from webscrap.yts_scrapper import YTSScrapper
from webscrap.enum.quality_type import QualityType
from webscrap.yts_searcher import YTSSearcher

class AutoTorrent:

    def __init__(self):
        self.scrapper = YTSScrapper()

    def start(self, input, allowed_qualities: List[QualityType]) -> list:
        self.searhcer = YTSSearcher(input=input)
        movie_list = self.searhcer.start_search()
        result_list = []
        for item in movie_list:
            scrap_result = self.scrapper.scrap(item.url, allowed_qualities)
            for torrent in scrap_result:
                result_list.append(torrent)
        return result_list