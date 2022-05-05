from Device import Device

class TV(Device):
    def __init__(self):
        super().__init__()
        self.addTag("channel",1)
        self.addTag("volume",0)

    def changeChannelDown(self):
        """channel channels down ลง เลื่อนลง ช่อง"""
        print("changeChannelDown is called!")
        tag = self.getTagByName("channel")
        tag.setValue(tag.getValue()-1)
        print(tag)

    def changeChannelUp(self):
        """channel channels up ขึ้น เลื่อนขึ้น ช่อง"""
        print("changeChannelUp! is called!")
        tag = self.getTagByName("channel")
        tag.setValue(tag.getValue()+1)
        print(tag)

    def decreaseVolume(self):
        """sound volume decrease softer lower ลด ลดเสียง เบา เบาเสียง เสียง"""
        print("decreaseVolume is called!")
        tag = self.getTagByName("volume")
        tag.setValue(tag.getValue()-1)
        print(tag)

    def increaseVolume(self):
        """sound volume increase louder higer เพิ่ม เพิ่มมเสียง ดัง ดังขึ้น เสียง"""
        print("increaseVolume is called!")
        tag = self.getTagByName("volume")
        tag.setValue(tag.getValue()+1)
        print(tag)