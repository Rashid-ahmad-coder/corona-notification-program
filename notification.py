from bs4 import BeautifulSoup
from plyer import notification
import requests
import time

def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="corona_icon.ico",
        timeout=10,
    )

def getdata(url):
    r=requests.get(url)
    return r.text

if __name__=="__main__":
    while True:
        myhtmlData=getdata('https://www.mohfw.gov.in/')
        soup =BeautifulSoup(myhtmlData, 'html.parser')
        print(soup.prettify())
        mystrData=""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            mystrData+=tr.get_text()
        mystrData=mystrData[1:]
        itemList=mystrData.split("\n\n")
        #print(itemList)
        states=['Uttar Pradesh','Maharashtra','Delhi']
        for item in itemList[0:35]:
            datalist=item.split('\n')
            if datalist[1] in states:
                #print(datalist)
                ntitle="Cases of Covid-19"
                ntext=f"{datalist[1]}:\n Active_cases: {datalist[2]}: Cure: {datalist[3]}:\n Death: {datalist[4]}: Confirmed_Cases: {datalist[5]}"
                notifyMe(ntitle, ntext)
                time.sleep(2)
        time.sleep(3600)