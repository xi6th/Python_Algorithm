"""

Expectation: 
    1. Returns highest value
    2. count the values 
"""



def birthdayCakeCandles(candles):
    highest_candle = max(candles)
    number_of_highest_candle = candles.count(highest_candle)
    return number_of_highest_candle
    # Write your code here

candles = [3, 2, 1, 3]
birthdayCakeCandles(candles)