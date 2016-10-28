#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import requests
import json


class HomeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        if args[1] is None:
            subject_id = '4'
            iran_news = requests.get('http://www.servicefarsi.com/api/news/4443819560110/4/item=4,page=1')
        else:
            subject_id = args[1]
            iran_news = requests.get('http://www.servicefarsi.com/api/news/4443819560110/4/item={0},page=1'.format(args[1]))
        iran_news = json.loads(iran_news.text)
        list_iran_news = []
        if iran_news['err'] == 0:
            list_iran_news = iran_news['res']

        city = requests.get('http://www.servicefarsi.com/api/news/4443819560110/2/')
        list_city = []
        city = json.loads(city.text)
        if city['err'] == 0:
            list_city = city['res']

        subject = requests.get('http://www.servicefarsi.com/api/news/4443819560110/1/')
        list_subject = []
        subject = json.loads(subject.text)
        if subject['err'] == 0:
            list_subject = subject['res']

        if args[0] is None:
            city_id = '17'
            city_news = requests.get('http://www.servicefarsi.com/api/news/4443819560110/4/item=17,page=1')
        else:
            city_id = str(args[0])
            city_news = requests.get('http://www.servicefarsi.com/api/news/4443819560110/4/item={0},page=1'.format(args[0]))

        city_news = json.loads(city_news.text)
        list_city_news = []
        if city_news['err'] == 0:
            list_city_news = city_news['res']
        self.render("home.html", list_states=list_iran_news, list_news=list_city_news, list_city=list_city, list_subject=list_subject, city_id=city_id, subject_id=subject_id)

    def post(self, *args, **kwargs):
        pass


class ShowMessage(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        news_data = requests.get('http://www.servicefarsi.com/api/news/4443819560110/7/item={0}'.format(args[2]))
        news_data = json.loads(news_data.text)
        self.render("show_news.html", news_data=news_data)

    def post(self, *args, **kwargs):
        pass
