class News:
     #the class that defines news objets

    def __init__(self, author, title, description, url, urlToImage, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

class Source:

    #the class that defines the source of objects

    def __init__(self, id, name, url):
        self.id = id 
        self.name = name
        self.url = url

class Category:

    #the class tha defines the categories of the objects

    def __init__(self, title, description, url , urlToImage, publishedAt):
        self.title = title
        self.description = description 
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt