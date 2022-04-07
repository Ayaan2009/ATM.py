import datetime

class Atm(object):
    def __init__ (self, color, transactionAmount, isCashAvailable):
        self.color = color
        self.transactionAmount = transactionAmount
        self.isCashAvailable = isCashAvailable
    def showTransactionDetails(self):
        print("Transaction Details")
        print(datetime.datetime.now())
        print(self.transactionAmount)

money = Atm("gray", 5000, True)
money.showTransactionDetails()
