class SingleYTSMovie:
    
    def __init__(self, title, year, url):
        self.title = title
        self.year = year
        self.url = url

    def __str__(self) -> str:
        return f'Title: {self.title}, Year: {self.year}, URL: {self.url}'