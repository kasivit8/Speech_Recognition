from Device import Device
import speech_recognition as sr
from collections import Counter
from utils import recognize_speech_from_mic, partOfSpeech
from LightBulb import LightBulb
from TV import TV
from dictionary import Dictionary
#from Websocket import ScadaWebsocketConnection

class Assistant():
    def __init__(self):
        super().__init__()
        #host = "wss://vrsmarthome.ap.ngrok.io/ws/tag/1/"
        #token = "eb3cf8ceb1bde8b2d540a8d9c17ac94e343b1f32"

        #self.SCADA = ScadaWebsocketConnection(host,token)

    def speechCommand(self, debug = False):
        # create recognizer and mic instances
        recognizer = sr.Recognizer()
        #print(sr.Microphone.list_microphone_names())
        microphone = sr.Microphone(device_index=2)

        guess = recognize_speech_from_mic(recognizer, microphone, "th")
        print("ANS")
        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))

        # show the user the transcription
        print("You said: {}".format(guess["transcription"]))

        pos = partOfSpeech(guess["transcription"])
        if debug:
            print(pos)
        dictionary = Dictionary()
        lightBulb = LightBulb()
        tv = TV()
        result = None
        #self.SCADA.connect()
        for word in pos:
            if word[1] == "PROPN" or word[1] == "NOUN":
                result = dictionary.find(word[0])
                if result == "LightBulb" or result == "TV":
                    break

        if debug:
            print(result)

        if result == "LightBulb":
            docString = dictionary.mapping(lightBulb)
            counter = [0 for x in range(len(docString))]
            i = 0
            for method in docString:
                keywords = method.split(" ")
                for word in pos:
                    if word[0] in keywords:
                        counter[i] += 1
                i += 1
            
            max_value = max(counter)
            max_index = counter.index(max_value)
            frequency = Counter(counter).most_common()
            "[(10, 3), (30, 2), (50, 1), (60, 1)]"
            if debug:
                print("max value: {} \nindex: {} \nMode: {}".format(max_value, max_index, frequency))
            for pair in frequency:
                if pair[0] == max_value and pair[1] == 1:
                    getattr(lightBulb, dictionary.methods[result][max_index])()

        elif result == "TV":
            docString = dictionary.mapping(tv)
            counter = [0 for x in range(len(docString))]
            i = 0
            for method in docString:
                keywords = method.split(" ")
                for word in pos:
                    if word[0] in keywords:
                        counter[i] += 1
                i += 1
            
            max_value = max(counter)
            max_index = counter.index(max_value)
            frequency = Counter(counter).most_common()
            "[(10, 3), (30, 2), (50, 1), (60, 1)]"
            if debug:
                print("max value: {} \nindex: {} \nMode: {}".format(max_value, max_index, frequency))
            for pair in frequency:
                if pair[0] == max_value and pair[1] == 1:
                    getattr(tv, dictionary.methods[result][max_index])()
                else:
                    raise Exception("Please try again.")

        else:
            #self.SCADA.close()
            raise Exception("Device is not found")