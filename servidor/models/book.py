class Book():
    def __init__(
            self,
            author  : str = "Unknown",
            country : str  = "Unknown",
            imageLink  : str  = "Unknown",
            language:  str  = "Unknown",
            link   : str  = "Unknown",
            pages  : int  = 0,
            title : str  = "Unknown",
            year : int = 0,
    ):
        self.author = author
        self.country = country
        self.imageLink = imageLink
        self.language = language
        self.link = link
        self.pages = pages
        self.title = title
        self.year = year
    
    def to_json(self) -> dict:
        return {
            "author" : self.author,
            "country" : self.country,
            "imageLink" : self.imageLink,
            "language" : self.language,
            "link" : self.link,
            "pages" : self.pages,
            "title" : self.title,
            "year" : self.year
        }

    @classmethod
    def from_json(cls, json)-> None:
        return Book(
            author=json["author"],
            country=json["country"],
            imageLink=json["imageLink"],
            language=json["language"],
            link=json["link"],
            pages=json["pages"],
            title=json["title"],
            year=json["year"]
        )