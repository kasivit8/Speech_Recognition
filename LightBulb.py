from Device import Device
from Websocket import setTag, getTag

class LightBulb(Device):
    def __init__(self):
        super().__init__()
        #self.addTag("onOff",0)
        #self.addTag("brightness",0)
        #self.addTag("color","#ff00ff")

    def lightOn(self):
        """light lights on เปิด เปิดไฟ ไฟ หลอดไฟ"""
        print("lightOn is called!")
        #tag = self.getTagByName("onOff")
        #tag.setValue(1)
        data = {"system": "CybrPhys", "name": "Hue1","tag": "onoff","value": 1}
        setTag(data)
        #print(tag)
        
    def lightOff(self):
        """light lights off ปิด ปิดไฟ ดับไฟ ไฟ หลอดไฟ"""
        print("lightOff is called!")
        #tag = self.getTagByName("onOff")
        #tag.setValue("off")
        data = {"system": "CybrPhys", "name": "Hue1","tag": "onoff","value": 0}
        setTag(data)
        #print(tag)

    def brightnessUp(self):
        """brightness increase add brighter up เพิ่ม เพิ่มแสง เพิ่มแสงสว่าง แสง แสงสว่าง"""
        print("brightnessUp is called!")
        #tag = self.getTagByName("brightness")
        #tag.setValue(tag.getValue()+10)
        data = {"system": "CybrPhys", "name": "Hue1","tag": "brightness"}
        value = getTag(data)
        print("value =", value)
        data = {"system": "CybrPhys", "name": "Hue1","tag": "brightness","value": int(value)+20}
        setTag(data)
        #print(tag)

    def brightnessDown(self):
        """brightness decrese lower down ลด ลดแสง ลดแสงสว่าง แสง แสงสว่าง"""
        print("brightnessDown is called!")
        #tag = self.getTagByName("brightness")
        #tag.setValue(tag.getValue()-1)
        data = {"system": "CybrPhys", "name": "Hue1","tag": "brightness"}
        value = getTag(data)
        print("value =", value)
        data = {"system": "CybrPhys", "name": "Hue1","tag": "brightness","value": int(value)-20}
        setTag(data)
        #print(tag)

    def changeColor(self):
        """color change เปลี่ยน เปลี่ยนสี"""
        pass