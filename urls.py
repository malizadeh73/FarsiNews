
from handler.home_handler import HomeHandler, ShowMessage
urls = [
    (r'/(\d+)?', HomeHandler),
    (r'/news/show/(.+)', ShowMessage),
]