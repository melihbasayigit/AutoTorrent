from typing import List
from torrent.torrent_manager import TorrentManager, CategoryType
from webscrap.yts_scrapper import YTSScrapper
from webscrap.enum.quality_type import QualityType
from webscrap.yts_searcher import YTSSearcher

class AutoTorrent:

    def __init__(self):
        self.scrapper = YTSScrapper()

    # Listeyi enum üyeleriyle eşleştirme fonksiyonu
    def map_to_enum(self, quality_list):
        mapped_enum = []
        for quality in quality_list:
            try:
                # Enum sınıfındaki değerlerle eşleşme
                enum_value = QualityType[f"_{quality}"]
                mapped_enum.append(enum_value)
            except KeyError:
                print(f"'{quality}' değeri QualityType enumunda yok.")
        return mapped_enum

    def start(self, input, allowed_qualities: List[QualityType]) -> list:
        self.searhcer = YTSSearcher(input=input)
        movie_list = self.searhcer.start_search()
        result_list = []
        for item in movie_list:
            scrap_result = self.scrapper.scrap(item, allowed_qualities)
            for torrent in scrap_result:
                result_list.append(torrent)
        return result_list
    
    def defaultStart(self, input, qualities: list) -> list:

        # Enum'a dönüştürülmüş liste
        mapped_enum_list = self.map_to_enum(qualities)
        return self.start(input=input, allowed_qualities=mapped_enum_list)