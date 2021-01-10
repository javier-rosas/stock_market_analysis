import json, websocket, ssl, candlestick, quotes


def run(candle, quote, params):
        
    # on_open: send authentication data and channel data
    def on_open(ws): 
        print("Opened Connection")
        # send authentication data 
        auth_data = {"action":"auth","params":"AKIJL74XBP2M5WEQBZ2L"}
        ws.send(json.dumps(auth_data))
        
        # send channel data
        channel_data = {
            "action":"subscribe",
            "params":params
        }
        ws.send(json.dumps(channel_data))

    
    # on_close: closed connection
    def on_close(ws):
        print("Closed Connection")


    # on_error: print error
    def on_error(ws, error):
        print(error)


    # on_message: print message
    def on_message(ws, message):
        if candle == True: 
            candlestick.get_bullish_candlestick(message)
        if quote == True: 
            quotes.get_ask_to_bid_ratio(message)

    stock_socket = "wss://alpaca.socket.polygon.io/stocks"
    ws = websocket.WebSocketApp(stock_socket, on_open=on_open, on_close=on_close, on_message=on_message, on_error=on_error)
    return ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
    



