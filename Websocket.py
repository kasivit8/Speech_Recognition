import json
import threading

import websocket
    
def intToHEX(value : int):
    return '#' + '{0:06X}'.format(int(value))

# WebSocket lib constructor
#websocket.enableTrace(True)

'''CLASS-BASED CONNECTION'''

class ScadaWebsocketConnection:
    def __init__(self, host, token):
        self.ws = websocket.WebSocketApp(
            host,
            on_open = self.on_open,
            on_message = self.on_message,
            on_error = self.on_error,
            on_close = self.on_close,
            header = [
                "Sec-WebSocket-Protocol: " + token
                ]
            )
        self.socket = threading.Thread(target= self.run_connection)
        self.message = []
        
    def on_open(self,ws):
        #print('Opening Websocket connection to SCADA server ... ')
        pass
        
    def on_message(self,ws,message):
        self.message.append(message)
        #print(message)
            
    def on_error(self,ws, error):
        print('Error on Connection:', error)

    def on_close(self,ws,errcode,message):
        #print("WebSocket Connection Closed")
        pass
            
    def run_connection(self):
        self.ws.run_forever()
        
    def connect(self):
        self.socket.start()
    
    def close(self):
        self.ws.close()

host = "wss://vrsmarthome.ap.ngrok.io/ws/tag/1/"
token = "eb3cf8ceb1bde8b2d540a8d9c17ac94e343b1f32"

SCADA = ScadaWebsocketConnection(host,token)
SCADA.connect()

def setTag(data):
    payload = json.dumps({"type" : "set_tag",
                            "tag" : "{}.{}.{}".format(
                                data["system"],data["name"],data["tag"]),
                            "value" : data["value"]})
    message = json.dumps({"message" : payload})
    SCADA.ws.send(message)
    SCADA.ws.close()

def getTag(data):
    payload = json.dumps({"type" : "get_tag",
                            "tag" : "{}.{}.{}".format(
                                data["system"],data["name"],data["tag"])})
    message = json.dumps({"message" : payload})
    SCADA.ws.send(message)
    while(not SCADA.message):
        pass
    return json.loads(json.loads(SCADA.message[0])["message"])["value"]
    #SCADA.ws.close()