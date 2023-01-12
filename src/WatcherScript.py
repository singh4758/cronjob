from src.model.watcher import Watcher
from src.model.user import User
from src.controller.priceScrapper import PriceScrapper


class WatcherScript:

  def __init__(self):
    self.watcherColl = Watcher()
    self.userColl = User()

  def watcherCursor(self):
    return self.watcherColl.find({})

  def run(self):
    for watcherData in self.watcherCursor():
      query = watcherData['productName']
      trackerData = watcherData['trackerData']
      price_scrapper = PriceScrapper(query)
      productsData = price_scrapper.get_scrapped_price()
      for tracker in trackerData:
        targetPrice = tracker["targetPrice"]
        userId = tracker["userId"]
        user = self.userColl.find_one({ "_id":  userId })
        userEmail = user.get("userEmail")
        productUrl = ""
        productImageURL = ""
        productName = ""
        lowestPrice = targetPrice
        for data in productsData:
          if data['price'] <= targetPrice:
            lowestPrice = data['price']
            productUrl = data['productURL']
            productImageURL = data["productImageURL"]
            productName = data["name"]
        if len(productName):
          print("productName "+ str(productName) +" lowestPrice "+str(lowestPrice) + " userEmail "+ str(userEmail))

    