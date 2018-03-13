import numpy as np
import pandas as pd

class Env():

    def __init__(self):
        self.state = 0
        self.income = 0.0
        self.holdingPrice = 0.0
        self.sellshortPrice = 0.0
        #self.file = pd.read_csv(fileName)

    def performAction(self, action, openPrice):
        
        if action == 1:
            # check current state
            assert self.state != 1

            if self.state == -1:
                self.income += self.sellshortPrice - openPrice
                self.sellshortPrice = 0.0
            elif self.state == 0:
                self.holdingPrice = openPrice

            self.state += 1
        
        elif action == -1:
            assert self.state != -1
            
            if self.state == 1:
                self.income += openPrice - self.holdingPrice
                self.holdingPrice = 0.0
            elif self.state == 0:
                self.sellshortPrice = openPrice
            
            self.state -= 1
        
        elif action == 0:
            return

    def finalIncome(self, closePrice):
        '''
            closePrice : The close-price of last day.
        '''
        
        if self.state == 1:
            self.income += closePrice - self.holdingPrice
            self.state = 0
        elif self.state == -1:
            self.income += self.sellshortPrice - closePrice
            self.state = 0
        
        return self.income
        