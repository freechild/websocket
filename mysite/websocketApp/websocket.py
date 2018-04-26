import sys
import json
import websocket

def add_channel(channel):
    json_data = json.dumps(
        {
            'event':'addChannel', 
            'channel':channel,
            'binary':'0'
        }
    )
    return json_data

def on_message(self,evt):
    print(evt)

def on_open(self):
    print('open')
    json_data1 = add_channel('ok_sub_spot_btc_usd_ticker')
    self.send(json_data1)

def on_error(self,evt):
    print (evt)

def on_close(self):
    print ('DISCONNECT')


def websocket_init():
    url = "wss://real.okcoin.com:10440/websocket/okcoinapi" 
    websocket.enableTrace(False)
    if len(sys.argv) < 2:
        host = url
    else:
        host = sys.argv[1]
    ws = websocket.WebSocketApp(url,
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close
                                )
    ws.on_open = on_open
    ws.run_forever()    