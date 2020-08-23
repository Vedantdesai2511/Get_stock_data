import websocket
import json
import ast
import config

stock_name_list = ['NFLX', 'ROKU', 'BYND', 'SQ', 'PYPL']  # You can add whatever stock ticker you like to watch
# here upto 200 tickers for every tick data and no limit for getting AM data

string_for_alpaca = ""

for i in stock_name_list:
    string_for_alpaca = string_for_alpaca + i + ','

print(string_for_alpaca[:-1])
sym = string_for_alpaca[:-1]
print(f'sym: {sym}')

string = ""

for i in stock_name_list:
    string = string + "T." + i + ', '

for i in stock_name_list:
    string = string + "AM." + i + ', '
string = string[: len(string) - 2]
string = '"' + string + '"'
print(string)


def on_open():
    print("opened")
    auth_data = {"action": "auth", "params": config.API_KEY}
    ws.send(json.dumps(auth_data))
    listen_message = {"action": "subscribe", "params": string}
    ws.send(json.dumps(listen_message))


def on_message(_, message):

    print(f'message: {message}')
    data = ast.literal_eval(message)  # This line converts message to dictionary so that we can use it in our trading
    # algorithm


def on_close():
    pass
    # start_algo()


socket = "wss://alpaca.socket.polygon.io/stocks"
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()
