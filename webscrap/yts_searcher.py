import requests
from bs4 import BeautifulSoup
from typing import List, Tuple
from webscrap.enum.websites import Websites
from webscrap.model.single_yts_movie import SingleYTSMovie

class YTSSearcher:
    def __init__(self, input:str):
        self.input_text = input

    def start_search(self) -> List[SingleYTSMovie]:
        url = self.url_creator()
        response = requests.get(url)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        movie_blocks = soup.find_all('div', class_='browse-movie-wrap')
        movie_list = []
        for movie_block in movie_blocks:
            movie_title = movie_block.find('a', class_='browse-movie-title').text.strip()
            movie_year = movie_block.find('div', class_='browse-movie-year').text.strip()
            movie_link = movie_block.find('a', class_='browse-movie-link')['href']
            movie = SingleYTSMovie(movie_title, movie_year, movie_link)
            movie_list.append(movie)
        return movie_list

    def url_creator(self) -> str:
        new_input = self.input_text.replace(' ', '%20')
        url = Websites.YTS_MX.value
        return url + f'browse-movies/{new_input}/all/all/0/latest/0/all'