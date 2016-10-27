
from handler.base_handler import HomeHandler, ShowMessage
urls = [
    (r'/(\d+)?/?(\d+)?', HomeHandler),
    (r'/news/show/(.+)', ShowMessage),
]