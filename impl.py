class Trader():

    def __init__(self):
        self.status = 0
        self.prevOpenPrices = []
        self.prevClosePrices = []
        self.fiveDaysAvg = 0.0

    def train(self, data):
        pass

    def non_increasing(self, L):
        return all(x>=y for x, y in zip(L, L[1:]))

    def non_decreasing(self, L):
        return all(x<=y for x, y in zip(L, L[1:]))
    
    def predict_action(self, data):
        # return a list
        action = [0]
        
        # previous open prices
        self.prevOpenPrices.append(data[0])
        # previous close prices
        self.prevClosePrices.append(data[3])

        if len(self.prevOpenPrices) > 4:
            self.prevOpenPrices.pop(0)

            #
            if len(self.prevClosePrices) > 5:
                self.prevClosePrices.pop(0)
                self.fiveDaysAvg = sum(self.prevClosePrices) / 5

            # if price going up, buy it
            if (self.non_decreasing(self.prevOpenPrices) and self.fiveDaysAvg < data[3]):
                if self.status != 1:
                    action[0] = 1
                    self.status += 1

            # if price going down, sell it 
            elif (self.non_increasing(self.prevOpenPrices) and self.fiveDaysAvg > data[3]):
                if self.status != -1:
                    action[0] = -1
                    self.status -= 1

            else:
                action[0] = 0

        return action    
        
        