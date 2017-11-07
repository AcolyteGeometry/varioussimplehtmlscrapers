from MenuT import MenuT
import json
import urllib.request
import re
from bs4 import BeautifulSoup

class qqVidScraper():

    baseurl = 'https://v.qq.com/x/page/'
    fnameappend = '-metadata.json'
    jsonenc = json.JSONEncoder()
    menut = MenuT()
    menu = [["QQ Video Scraper","Select an option:"],["Scrape Video", 1], ["Exit", 2]]
    menuid = [["QQ Video Scraper", "Input video ID:"]]

    def showMenu(self):
        mopt = self.menut.stoi(self.menut.showMenu(self.menu))
        if(mopt == 1):
            self.vididMenu()
        elif(mopt == 2):
            exit(0)

    def vididMenu(self):
        mopt = self.menut.showMenu(self.menuid)
        self.scrapeVideo(mopt)
        self.showMenu()

    def scrapeVideo(self, vidid, stdout = True):
        dict = {'vidid': vidid, \
                'title': None, \
                'desc': None, \
                'uploaddate':None,\
                'username':None, \
                'channel': None, \
                'origurl':None,\
                'uploader':None,\
                'date':None}
        url = self.baseurl + vidid + '.html'
        page = urllib.request.urlopen(url)
        # page.geturl() # checks for final url after redirect
        soup = BeautifulSoup(page, 'html.parser')

        dict['username'] = soup.find('span', attrs={'class': 'user_name'}).text.strip()
        dict['userlink'] = soup.find("a", href=re.compile("^http://v.qq.com/vplus/[a-z0-9]*$"))\
            .text.get('href') # gets the channel url link

        dict['date'] = soup.find('meta', attrs={'itemprop': 'datePublished'}).text.strip()["content"]
        dict['origurl'] = soup.find('meta', attrs={'itemprop': 'url'}).text.strip()["content"]
        dict['title'] = soup.find('meta', attrs={'itemprop': 'name'}).text.strip()["content"]
        dict['desc'] = soup.find("meta", {"name": "description"}).text.strip()["content"]

        page = urllib.request.urlopen(dict['userlink'].get('href'))
        dict['uploader'] = BeautifulSoup(page, 'html.parser').html.head.title.text.strip()\
            .replace('的个人频道 - 视频列表', '', 1)
        if(stdout):
            print("Uploader: " + dict['uploader'])
            print("Channel: " + dict['userlink'])
            print("Upload Date: " + dict['date'])
            print("Description: " + str(dict['desc'])) # checks the value of content, within meta name=description
            print("Original URL: " + str(dict['origurl']))

        return dict

    def writeFile(self, data):
        filename = data['title'] + "-" + data['vidid'] + self.fnameappend
        f = open(filename, 'w')
        f.write(self.getJSON(data))
        f.close()

    def getJSON(self, data):
        return self.jsonenc.encode({data['vidid']: data})

qqVidScraper().menut.showMenu()