# You can write code above the if-main block.
import numpy as np
import pandas as pd
from sklearn.svm import SVR 
import csv
import itertools
from Env import Env
#import matplotlib.pyplot as plt

def testDataResult(actionFile):
    
    testEnv = Env()
    actionList = []
    actIndex = 0
    closePrice = 0.0

    # read actions
    df = pd.read_csv(actionFile, names = ['Action'])
    for index, row in df.iterrows():
        actionList.append(row[0])

    testData = pd.read_csv(args.testing, 
        names = ["Open", "High", "Low", "Close"])
    for index, price in testData.iterrows():
        # Use the next day's price to buy stock, ignore 1st day stock price 
        if index != 0:
            testEnv.performAction(actionList[actIndex], price[0])
            actIndex += 1
            closePrice = price[3]

    print("Final income:", testEnv.finalIncome(closePrice))


if __name__ == '__main__':
    # You should not modify this part.
    import argparse
 
    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                        default='dataset/training_data.csv',
                        help='input training data file name')
    parser.add_argument('--testing',
                        default='dataset/testing_data.csv',
                        help='input testing data file name')
    parser.add_argument('--output',
                        default='dataset/output.csv',
                        help='output file name')
    args = parser.parse_args()
      

    testData =  pd.read_csv(args.testing, 
        names = ["Open", "High", "Low", "Close"])

    '''
        TODO: implement trader model
    '''

    #trader = Trader()
    #trader.train(training_data)
      
    with open(args.output, 'w') as output_file:
        for index, row in testData.iterrows():
            
            # We will perform your action as the open price in the next day.
            #action = trader.predict_action(datum)
            
            if index == (len(testData) - 1): break
            writer = csv.writer(output_file)
            writer.writerow("0")
 
            # this is your option, you can leave it empty.
            # trader.re_training(i)
    
    # test the base case
    testDataResult("dataset/base.csv")