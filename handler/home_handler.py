import tornado.web
import requests
import json


class HomeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        states = requests.get('http://www.servicefarsi.com/api/news/4443819560110/4/item=0,page=1')
        # print(states.text)
        list_states = []
        states = json.loads(states.text)
        if states['err'] == 0:
            list_states = states['res']

        if args[0] is not None:
            state_news = requests.get('http://www.servicefarsi.com/api/news/4443819560110/4/item={0},page=1'.format(args[0]))
        else:
            state_news = requests.get('http://www.servicefarsi.com/api/news/4443819560110/4/item=17,page=1')
            # news default for tehran
        # print(state_news.text)
        state_news = json.loads(state_news.text)
        list_news = []
        if state_news['err'] == 0:
            list_news = state_news['res']

        self.render("home.html", list_states=list_states, list_news=list_news)

    def post(self, *args, **kwargs):
        pass


class ShowMessage(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        news_data = requests.get('http://www.servicefarsi.com/api/news/4443819560110/7/item={0}'.format(args[0]))
        print(news_data.text)
        news_data = json.loads(news_data.text)
        if news_data['err'] == 1:
            news_data = {}  # when api return error
        self.render("show_news.html", news_data=news_data)

    def post(self, *args, **kwargs):
        pass
