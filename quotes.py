import json
import send_email

# Helper function for getting the average bid-to-ask ratio 
list_of_ratios = []
average_ratio = None
def average_ratio_func():
    global average_ratio
    print(len(list_of_ratios))
    if len(list_of_ratios) == 30: 
        average_ratio = sum(list_of_ratios) / len(list_of_ratios)


# Get average ratios 
list_of_bullish_ratios = []
def get_ask_to_bid_ratio(message):

    # Receiving payload from polygon response
    response = json.loads(message)

    # Calculating bid data
    bid_size = response[0]['bs']
    bid_price = response[0]['bp']
    
    # Calculating ask data
    ask_size = response[0]['as']
    ask_price = response[0]['ap']

    # Calculating bid and ask totals (bid/ask price * bid/ask size)
    bid_total = bid_size * bid_price
    ask_total = ask_size * ask_price
    print("bid total ", bid_total)
    print("ask total ", ask_total)
    
    # Calculating ask to bid ratio 
    ask_to_bid_ratio = ask_total / bid_total
    print("Recurrent ask to bid ratio:", ask_to_bid_ratio)

    # First 30 instances of average ratios
    list_of_ratios.append(ask_to_bid_ratio)
    print("average ratio (first 30 instances) = ", average_ratio)
    average_ratio_func()

    if (average_ratio != None) and (ask_to_bid_ratio * 1.3 > average_ratio):
        list_of_bullish_ratios.append(ask_to_bid_ratio)

    if len(list_of_bullish_ratios) >= 3: 
        # execute trade and send alert text/email 
        send_email.send_email()
       









