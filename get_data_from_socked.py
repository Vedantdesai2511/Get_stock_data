import websocket
import json
import ast
import config

stock_name_list = ['NFLX', 'ROKU', 'BYND', 'SQ', 'PYPL']  # You can add whatever stock ticker you like to watch
# here, You can add unto 200 tickers for every tick data and there is no limit for getting AM data

string_for_alpaca = ""  # Initialize string to generate the string to pass on to the API call for getting candle
# historical data for the stocks in stock_name_list

for i in stock_name_list:  # generate the string to pass on to the API call for getting candle historical data for
    # the stocks in stock_name_list
    string_for_alpaca = string_for_alpaca + i + ','

print(string_for_alpaca[:-1])
sym = string_for_alpaca[:-1]
print(f'sym: {sym}')

string = ""  # Initialize string to generate the string to pass on to the API call for getting AM and tick data for
# the stocks in stock_name_list

for i in stock_name_list:  # generate the string to pass on to the API call for getting ticker data for the
    # stocks in stock_name_list
    string = string + "T." + i + ', '

for i in stock_name_list:  # generate the string to pass on to the API call for getting AM (minute candle data) data
    # for the stocks in stock_name_list
    string = string + "AM." + i + ', '
string = string[: len(string) - 2]
string = '"' + string + '"'
print(string)


def on_open():
    """
    This function is called when the socket is opened
    """
    print("opened")
    auth_data = {"action": "auth", "params": config.API_KEY}
    ws.send(json.dumps(auth_data))
    listen_message = {"action": "subscribe", "params": string}
    ws.send(json.dumps(listen_message))


def on_message(_, message):
    """
    This function runs when socket recives any message
    :param _: message
    :param message: message the socket got
    """

    print(f'message: {message}')
    data = ast.literal_eval(message)  # This line converts message to dictionary so that we can use it in our trading
    # algorithm


def on_close():
    """
    This function runs when the socket is closed
    """
    pass


socket = "wss://alpaca.socket.polygon.io/stocks"  # The link of the socket
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)  # Initialize the socket
ws.run_forever()  # Run the socket - in this case we are using socket as a readio from ehich we will take useful data
# - hence here we are running the socket forever
