from bs4 import BeautifulSoup
import re
from datetime import datetime, timezone, timedelta
import requests


class FortuneTelling(object):
    def __init__(self, sign):
        self.sign = sign
        self.url = "https://fortune.yahoo.co.jp/12astro/" + self.sign
        self.html = requests.get(self.url)
        self.soup = BeautifulSoup(self.html.content, "html.parser")
        self.points = self.soup.find_all(src=re.compile("s.yimg.jp/images/fortune/images/common/yftn_param"))
        self.totalPoint = re.findall('"([^"]*)"',str(self.points[0]))[0]  #総合の点数
        self.lovePoint = re.findall('"([^"]*)"',str(self.points[1]))[0]  #恋愛運の点数
        self.moneyPoint = re.findall('"([^"]*)"',str(self.points[2]))[0]  #金運の点数
        self.workPoint = re.findall('"([^"]*)"',str(self.points[3]))[0]  #仕事運の点数
        self.rank = str(self.soup.select('strong')[2].text)[0:2]  #総合順位
        
        self.totalPoint = round((int(re.match(r'.*点中(.*?)点.*', self.totalPoint).group(1))/20))
        self.lovePoint = round((int(re.match(r'.*点中(.*?)点.*', self.lovePoint).group(1))/2))
        self.moneyPoint = round((int(re.match(r'.*点中(.*?)点.*', self.moneyPoint).group(1))/2))
        self.workPoint = round((int(re.match(r'.*点中(.*?)点.*', self.workPoint).group(1))/2))
        
        self.total = self.soup.find_all(class_=re.compile('yftn12a-md48'))
        self.totalSummary = str(self.total[0].find('dt').text)  #一日の運勢の総括
        self.totalDetail = str(self.total[0].find('dd').text)  #一日の運勢詳細
        self.act = str(self.total[1].find('dd').text) #開運のおまじない
        
        self.love = self.soup.find_all(id=re.compile('lnk02'))
        self.loveDetail = self.love[0].find('p').text  #恋愛運詳細

        self.money = self.soup.find_all(id=re.compile('lnk03'))
        self.moneyDetail  = self.money[0].find('p').text  #金運詳細

        self.work = self.soup.find_all(id=re.compile('lnk04'))
        self.workDetail = self.work[0].find('p').text  #仕事運詳細

        self.JST = timezone(timedelta(hours=+9), 'JST')  #日本時間に合わせる
        
        

    def CountStar(self, point):
        stars = ''
        for i in range(5):
            if point > 0:
                point -= 1
                stars += "★"
            else:
                stars += "☆"
        return stars

    
    def arrangeText(self, text):
        if len(text)>140:
            self.text = text[0:140]
            self.text = self.text[0:self.text.rfind("。")+1]
        else:
            self.text = text
        return self.text

    def LoveText(self):
        self.dt_now = datetime.datetime.now(self.JST)
        self.lovetext =  str(self.dt_now.month) + "月" + str(self.dt_now.day) + "日のしし座🦁\n恋愛運　" + self.CountStar(self.lovePoint) + "\n\n" + self.loveDetail
        return self.arrangeText(self.lovetext)


    def MoneyText(self):
        self.dt_now = datetime.datetime.now(self.JST)
        self.moneytext = str(self.dt_now.month) + "月" + str(self.dt_now.day) + "日のしし座🦁\n金運　　" + self.CountStar(self.moneyPoint) + "\n\n" + self.moneyDetail
        return self.arrangeText(self.moneytext)


    def WorkText(self):
        self.dt_now = datetime.datetime.now(self.JST)
        self.worktext = str(self.dt_now.month) + "月" + str(self.dt_now.day) + "日のしし座🦁\n仕事運　" + self.CountStar(self.workPoint) + "\n\n" + self.workDetail
        return self.arrangeText(self.worktext)


    def TotalText(self):
        self.dt_now = datetime.datetime.now(self.JST)
        self.totaltext = str(self.dt_now.month) + "月" + str(self.dt_now.day) + "日のしし座🦁\n総合運　　" + self.CountStar(self.totalPoint) + "\n\n" + self.totalDetail
        return self.arrangeText(self.totaltext)     


    def Text(self):
        self.dt_now = datetime.datetime.now()
        self.summarytext = str(self.dt_now.month) + "月" + str(self.dt_now.day) + "日のしし座🦁の順位は" + self.rank + '!\n\n' + self.totalSummary + "\n" + "総合運　" + self.CountStar(self.totalPoint) + "\n" + "恋愛運　" + self.CountStar(self.lovePoint) + "\n" + "金運　　" + self.CountStar(self.moneyPoint) + "\n" + "仕事運　" + self.CountStar(self.workPoint) + "\n\n" + "開運のおまじない\n" + self.act
        return self.arrangeText(self.summarytext)