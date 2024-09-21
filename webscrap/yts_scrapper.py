import requests
from bs4 import BeautifulSoup
from typing import List, Tuple
from webscrap.enum.quality_type import QualityType, QualityName
from webscrap.model.single_yts_torrent import SingleYTSTorrent
from webscrap.model.single_yts_movie import SingleYTSMovie

class YTSScrapper():

    def __init__(self):
        pass

    def __use_filters(self, torrent:SingleYTSTorrent, allowed_qualities: List[QualityType]) -> bool: # Not Working now 
        if len(allowed_qualities) == 0:
            return True
        for quality in allowed_qualities:
            if quality.value in torrent.quality_size.strip():
                return True
        return False
    
    def scrap(self, item: SingleYTSMovie, allowed_qualities: List[QualityType]) -> List[SingleYTSTorrent]:
        response = requests.get(item.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        torrents = soup.find_all('div', class_='modal-torrent')
        results = []
        for torrent in torrents:
            size = torrent.find('div', class_='modal-quality').text.strip()
            quality = torrent.find_all('p', class_='quality-size')[0].text.strip()
            magnet_link = torrent.find('a', class_='magnet-download')['href']
            torrent_item = SingleYTSTorrent(item.title, item.year, item.url, magnet_link, quality, size)
            if self.__use_filters(torrent_item, allowed_qualities):
                results.append(torrent_item)
        return results