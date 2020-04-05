from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon='D:/Python/projects/CoronaNotification/1.ico ',
        timeout=6
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    while True:
        # notifyMe('Shishir', "lets Stop")
        myHtmlData = getData('https://www.worldometers.info/coronavirus/')
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        myDataStr = ""
        for table in soup.find_all('table'):
            # print(table.get_text())
            myDataStr += table.get_text()
            myDataStr = myDataStr[1:]
            itemList = myDataStr.split("\n\n\n")

            country = ['Bangladesh', 'India', 'Italy', 'Spain']

            for item in itemList:
                datalist = item.split('\n')
                if datalist[0] in country:
                    # print(datalist)
                    nTitle = "Cases Of Covid-19"
                    nText = f"{datalist[0]}:Affect:{datalist[1]}:\n New:{datalist[2]}:\n Deaths:{datalist[3]}:&" \
                            f"New Deaths:{datalist[4]}:\n Tests:{datalist[10]} "
                    notifyMe(nTitle, nText)
                    time.sleep(4)

            time.sleep(3600)