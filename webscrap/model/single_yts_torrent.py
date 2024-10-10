class SingleYTSTorrent:

    def __init__(self, title: str, year: str, website_url: str, magnet_url: str, quality_name: str, 
                 quality_size: str, file_size: str, cover_picture: str, movie_category: str) -> None:
        self.title = title
        self.year = year
        self.website_url = website_url
        self.magnet_url = magnet_url
        self.quality_name = quality_name
        self.quality_size = quality_size
        self.file_size = file_size
        self.cover_picture = cover_picture
        self.movie_category = movie_category

    def __str__(self) -> str:
        return (
            f"Title: {self.title}\n"
            f"Year: {self.year}\n"
            f"Website URL: {self.website_url}\n"
            f"Magnet URL: {self.magnet_url}\n"
            f"Quality Name: {self.quality_name}\n"
            f"Quality Size: {self.quality_size}\n"
            f"File Size: {self.file_size}\n"
            f"Cover Picture: {self.cover_picture}\n"
            f"Movie Category: {self.movie_category}"
        )