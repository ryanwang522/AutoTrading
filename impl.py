class Trader():

    def __init__(self):
        self.status = 0
        self.prevOpenPrices = []

    def train(self):
        pass

    def non_increasing(self, L):
        return all(x>=y for x, y in zip(L, L[1:]))

    def non_decreasing(self, L):
        return all(x<=y for x, y in zip(L, L[1:]))
    
    def predict_action(self, data):
        # return a list
        action = [0]
        
        # previous 3 days open prices
        self.prevOpenPrices.append(data[0])
        
        if len(self.prevOpenPrices) > 4:
            self.prevOpenPrices.pop(0)

            # if price going up, buy it. 
            if (self.non_decreasing(self.prevOpenPrices)):
                if self.status != 1:
                    action[0] = 1
                    self.status += 1

            # if price going down, sell it 
            elif (self.non_increasing(self.prevOpenPrices)):
                if self.status != -1:
                    action[0] = -1
                    self.status -= 1

            else:
                action[0] = 0

        return action    
        
        