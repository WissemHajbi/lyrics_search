import requests
import bs4
import os
from pathlib import Path

def space(sentence):
    ind = sentence.find(' ')
    while ind > -1:
        sentence=sentence[:ind]+sentence[ind+1:]
        ind = sentence.find(' ')
    return sentence.lower()

def lyricssearch(songname,singer):
    title = '{} : {}'.format(singer, songname)
    try:
        Url = 'https://www.azlyrics.com/lyrics/{}/{}.html'.format(space(singer), space(songname))
        request = requests.get(Url)
        soup = bs4.BeautifulSoup(request.content, 'html.parser')
        div = soup.find('div', class_='col-xs-12 col-lg-8 text-center')
        lyricsDiv = div.find('div', class_='').getText()
        input = {'title':title,'lyrics':lyricsDiv}
        return input
    except:
        input={'error':'theres an error with your input'}
        return input
   
