
from handler.base_handler import HomeHandler, ShowMessage
urls = [
    (r'/(\d+)?/?(\d+)?', HomeHandler),
    (r'/?(\d+)?/?(\d+)?/news/show/(.+)', ShowMessage),
]