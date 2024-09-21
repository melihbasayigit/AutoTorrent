class SingleYTSTorrent:

    def __init__(self, title:str, year:str, website_url:str, magnet_url:str, quality_name:str, quality_size:str) -> None:
        self.title = title
        self.year = year
        self.website_url = website_url
        self.magnet_url = magnet_url
        self.quality_name = quality_name
        self.quality_size = quality_size

    def __str__(self) -> str:
        return (
        f"Title: {self.title}\n"
        f"Year: {self.year}\n"
        f"Website URL: {self.website_url}\n"
        f"Magnet URL: {self.magnet_url}\n"
        f"Quality Name: {self.quality_name}\n"
        f"Quality Size: {self.quality_size}"
    )