import urllib2, json
THRESHOLD = 0.00

class GiftCard:
    def __init__(self, name, amount, buyRate, sellRate):
        self.name = name
        self.amount = amount
        self.buyRate = buyRate
        self.sellRate = sellRate
    def __str__(self):
        return "Name: "+self.name+" Amount: "+str(self.amount)+" Buy Discount: "+str(self.buyRate)+" Sell Rate: "+str(self.sellRate)

def MakeRequest():
    url = "http://www.giftcardwiki.com/giftcards/data/alldata/"
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    return response.read()

def ParseData(szData, threshold):
    vecResults = []
    data = json.loads(szData)
    for gc in data:
        if 1-float(gc['buyDiscount'])-float(gc['sellRate']) <= threshold:
            giftcard = GiftCard(gc['name'], gc['amount'], gc['buyDiscount'], gc['sellRate'])
            vecResults.append(giftcard)
            
    return vecResults

if __name__ == '__main__':
    szData = MakeRequest()
    vecResults = ParseData(szData, THRESHOLD)
    if len(vecResults) > 0:
        print("Found the following results: ")
        for gc in vecResults:
            print (gc)
    else:
        print ("No gift cards found")