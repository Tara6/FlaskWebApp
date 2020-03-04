import requests
from bs4 import BeautifulSoup
import statistics

def findAverage(pricelist):
    for i in pricelist:
        average = statistics.mean(pricelist)
        averageround = str(round(average, 2))
        return averageround

def scrapePS4():
    response = requests.get("https://www.trademe.co.nz/gaming/playstation-4/consoles?buy=buynow&page1")
    soup = BeautifulSoup(response.text,"html.parser")
    itemlist = soup.findAll("div", {"class":"supergrid-listing"})
    cnt = len(itemlist)

    PS4list = []
    intbuynowList = []
    for item in itemlist:      
        try:
           item_title = item.find("div", {"class":"title"}).text.strip()
           item_buynow = item.find("div", {"class":"listingBuyNowPrice"}).text.strip()
           intbuynow = float(item_buynow[1:])
           PS4list.append({"Title" : item_title, "Price" : item_buynow})
           intbuynowList.append(intbuynow)
        except:
           print("item parse failed:", item)
    
    return PS4list




