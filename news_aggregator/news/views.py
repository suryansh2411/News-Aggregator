from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Getting news from Times of India

tie_r = requests.get("https://indianexpress.com/article/explained/india-coronavirus-cases-explained-delhi-mumbai-covid-cases-deaths-6475436/")
tie_soup = BeautifulSoup(tie_r.content, 'html5lib')
tie_headings = tie_soup.find_all('p')

tie_headings = tie_headings[0:3]+tie_headings[4:6] + tie_headings[8:12]

tie_news = []
for th in tie_headings:
	tie_news.append(th.text)




def index(req):
    return render(req, 'news/index.html', {'tie_news':tie_news})