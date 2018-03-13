# AutoTrading
This is for DSAI homework1

# Think
I'm a beginner of machine learning & data science. I've read some linear regression model on Internet, practicing some of it by scikit-learn.

However, in this HW, we cannot use previous data to predict the next day price (I think it's meaningless), so I return to the naive method - "Find and try to figure out the trend".

After find out the trend, I buy stock at low price and sell it at higher price. In the other hand, I sell out stock at high price and buy it back at lower price. 

# Model
I use previous four days open price to decide whether the stock is going up or down.
Also, by using previous five days average price to stable the buy/sell action. 
