#This is a general scaffolding for you to play with your finance algorithms

from yahoo_finance import Share

global stocks_owned
stocks_owned = {} #Create a dictionary to put your stocks in
global bankroll
bankroll = 100000000 #The amount of of dough you start with

                #TIME TO RIDE THE GRAAVY TRAIN



#Buy function, pass in string that has the stock symbol as first argument
#Then put in number of shared to buy 
#Example buy('YHOO',30) would buy 30 yahoo shares



def buy(symbol,number_to_buy):
    global bankroll 
    global stocks_owned
    already_owned = False
    stock = Share(symbol)
    stock.refresh() #If it runs like crap its this line 
    stock_value = float(stock.get_price())*float(number_to_buy)
    
    if(stock_value<bankroll): #can buy  stocks if you have $
        
        bankroll = bankroll-stock_value
        for key, value in stocks_owned.items(): 
            if(key == symbol):
                stocks_owned[key] += number_to_buy 
                already_owned = True
                
        if(already_owned != True):
            stocks_owned[symbol] = number_to_buy
                
    else:
        print("You don't have the dough to buy a "+str(number_to_buy)+ " of "+symbol)
        
        
def sell(symbol,number_to_sell):
    global bankroll 
    global stocks_owned
    stock = Share(symbol)
        
    for key, value in stocks_owned.items(): 
        if(key == symbol):
            if(stocks_owned[symbol]>number_to_sell):
                stocks_owned[key] -= number_to_sell
                stock.refresh() #If it runs like crap its this line 
                stock_value = float(stock.get_price())*float(number_to_sell)
                bankroll = bankroll+stock_value
                break
            else:
                print("You don't own enough of "+symbol+" to sell")
    
    
#Example of using the code. Study the outputs, you'll get it    
print(bankroll)
buy('YHOO',30000)
buy('AAPL',1000)
buy('JNJ',1000)
print(stocks_owned)
print(bankroll)
print("--------------------------")

sell('AAPL',500)
print("Bankroll after selling " + str(bankroll))
print(stocks_owned)


#Below this section you can add your trading algorithms