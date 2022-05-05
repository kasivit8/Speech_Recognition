class Dictionary:
    def __init__(self):
        self.device = {
            "TV": "television tv ทีวี โทรทัศน์",
            "LightBulb": "bulb lightbulb ไฟ หลอดไฟ เปิดไฟ ปิดไฟ เพิ่มแสง ลดแสง แสงไฟ"
        }
        self.methods = {
            "TV": ["changeChannelDown", "changeChannelUp", "decreaseVolume", "increaseVolume"],
            "LightBulb": ["lightOn", "lightOff", "brightnessUp", "brightnessDown", "changeColor"]
        }

    def find(self, word):
        for key, value in self.device.items():
            val = value.split(" ")
            if word in val:
                return key
        return None

    def mapping(self,object):
        docString = []
        name = type(object).__name__
        for method in self.methods[name]:
            docString.append(getattr(object, method).__doc__)
        return docString