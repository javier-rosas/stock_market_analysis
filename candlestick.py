import json

# Helper function for getting the average candlestick size
list_of_tick_differences = []
average_candlestick = None
def average_candlestick_func():
    global average_candlestick
    print(len(list_of_tick_differences))
    if len(list_of_tick_differences) == 30: 
        average_candlestick = sum(list_of_tick_differences) / len(list_of_tick_differences)
    

# Getting bullish candlesticks (1.7 * the average candlestick size)
list_of_bullish_candlesticks = []
bullish_stock = False
def get_bullish_candlestick(message):
    global bullish_stock

    response = json.loads(message)
    tick_open = response[0]['o']
    tick_close = response[0]['c']

    
    tick_difference = tick_close - tick_open
    list_of_tick_differences.append(abs(tick_difference))
    
    print("average candlestick = ", average_candlestick)
    average_candlestick_func()
    if (average_candlestick != None) and (tick_difference > 0) and (tick_difference * 1.7 > average_candlestick):
            list_of_bullish_candlesticks.append(tick_difference)
    
    if len(list_of_bullish_candlesticks) >= 3: 
        # execute trade and send alert text/email 
        bullish_stock = True 
    
    print("Tick Open:", tick_open, "Tick Close:", tick_close)
    


