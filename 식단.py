###pip install requests
###pip install bs4
###pip install python-telegram-bot
import telegram
토큰 = "1460256695:AAFbMqwAwPs7Wd8qR3BhO0syOFxRzvocRZQ"
봇 = telegram.Bot(token=토큰)

for i in 봇.getUpdates():
    print(i.message)
import datetime
import requests
import bs4

현재 = str(datetime.datetime.now())
print(현재)
날 = 현재[0:4] + 현재[5:7] + 현재[8:10]
# print(날)
html = requests.get("http://school.cbe.go.kr/ds-e/M01030602/list?ymd="+날)
# print(html.text)

수프 = bs4.BeautifulSoup(html.text,"html.parser")
트롤 = 수프.find("a", href="/ds-e/M01030602/list?ymd=ymd="+날)
식단리스트 = 트롤.find_all("li")

식단 = ''
for i in 식단리스트:
    식단 = 식단 + i.text + "\n"

if 식단 == "":
    식단 = "오늘은 급식이 없네요..."
else:
    봇.sendMessage("1452976504",식단)
