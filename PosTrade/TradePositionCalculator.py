import collections

class TradePositionCalculator:

  def __init__(self):
    self.buyQ = collections.deque()
    self.sellQ = collections.deque()
    self.pnl = 0.0
    self.openPosition = 0.0

  def calculateFIFoPNL(self):
    while len(self.buyQ) > 0 and len(self.sellQ) > 0 :
      resi = [0.0, 0.0] #variable can be removed but becomes less explanatory.
      buy = self.buyQ.pop()
      sell = self.sellQ.pop()
      qtyValue = buy[0] + sell[0]
      if(qtyValue > 0.0):
        resi = [qtyValue , buy[1]]
        self.pnl  = self.pnl + abs(sell[0])*(sell[1] - buy[1])
      else:
        resi = [qtyValue, sell[1]]
        self.pnl = self.pnl + buy[0]*(sell[1] - buy[1])
      if resi[0] > 0.0:
        self.buyQ.append(resi)
      elif resi[0] < 0.0:
        self.sellQ.append(resi)
 
  
  def update(self, quantity, price):
    if quantity >0.0:
      self.buyQ.appendleft([quantity, price])
    else:
      self.sellQ.appendleft([quantity, price])
  
  def getRealizedPNL(self):
    return self.pnl
  
  def getOpenPosition(self):
    return self.openPosition


stockAcalculator = TradePositionCalculator()

with open('G:/projects/py/testFiles/trades.txt') as f:
  next(f)
  for line in f:
    each = [float(x) for x in line.split()]
    stockAcalculator.update(each[0], each[1])
    stockAcalculator.calculateFIFoPNL()
    print(stockAcalculator.getRealizedPNL())