class SingleYTSTorrent:

    def __init__(self, magnet_url:str, quality_name:str, quality_size:str) -> None:
        self.magnet_url = magnet_url
        self.quality_name = quality_name
        self.quality_size = quality_size

    def __str__(self) -> str:
        return f"quality_name: {self.quality_name}\nquality_size: {self.quality_size}\nmagnet_url: {self.magnet_url}"