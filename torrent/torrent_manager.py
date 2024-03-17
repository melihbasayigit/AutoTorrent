import os
from dotenv import load_dotenv
import requests

from torrent.category_type import CategoryType
from torrent.errors import *

class TorrentManager:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        # qBittorrent Web UI credentials
        self.username, self.password, self.base_url = self.get_env_values()

        if not (self.username and self.password and self.base_url):
            raise EnvError("Please provide QB_USERNAME, QB_PASSWORD, and QB_WEB_UI in the .env file.")

        # Global settings
        self.gl_download_limit = 9500 * 1024  # Unit in bytes/second
        self.gl_upload_limit = 150 * 1024  # Unit in bytes/second
        self.gl_seeding_time_limit = 10080  # Unit minute. 10080 minutes is equal to 1 week.

        # Login to qBittorrent
        self.cookie = None
        self.login_to_qbittorrent()

    def get_env_values(self):
        # qBittorrent Web UI credentials
        username = os.getenv('QB_USERNAME')
        password = os.getenv('QB_PASSWORD')
        base_url = os.getenv('QB_WEB_UI')
        return username, password, base_url

    def login_to_qbittorrent(self):
        # Login to qBittorrent
        login_url = self.base_url + '/api/v2/auth/login'
        login_data = {'username': self.username, 'password': self.password}
        response = requests.post(login_url, data=login_data)

        # Extract the cookie for subsequent requests
        self.cookie = response.cookies.get('SID')

    def add_torrent(self, magnet_link, category_type: CategoryType):
        if not self.cookie:
            self.login_to_qbittorrent()  # Session check if necessary re-login process

        # Add torrent using magnet link
        add_torrent_url = self.base_url + '/api/v2/torrents/add'
        add_torrent_data = {'urls': magnet_link,
                            'upLimit': self.gl_upload_limit,
                            'dlLimit': self.gl_download_limit,
                            'seedingTimeLimit': self.gl_seeding_time_limit,
                            'savepath': category_type.value}
        headers = {'Cookie': f'SID={self.cookie}'}
        requests.post(add_torrent_url, data=add_torrent_data, headers=headers)

    def get_torrents(self) -> any:
        if not self.cookie:
            self.login_to_qbittorrent()  # Session check if necessary re-login process

        # Add torrent using magnet link
        torrent_list_url = self.base_url + '/api/v2/torrents/info?sort=added_on&reverse=true'
        headers = {'Cookie': f'SID={self.cookie}'}
        response = requests.get(torrent_list_url, headers=headers)
        return response.json()
