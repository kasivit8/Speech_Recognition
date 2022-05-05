from Tag import Tag

class Device(object):
    def __init__(self, name="", address="", tags = []):
        self.name = name
        self.address = address
        self.tags = tags

    def addTag(self, tag, value=None):
        self.tags.append(Tag(tag, value))

    def changeTag(self, original_tag, new_tag, value):
        try:
            for tag in self.tags:
                if tag.getTag() == original_tag:
                    if new_tag != None:
                        tag.setTag(new_tag)
                    if value != None:
                        tag.setValue(value)
        except:
            raise Exception("changeTag() has failed.")
        
    def getDevice(self):
        return self.tags

    def getTagByName(self, name):
        for tag in self.tags:
            if tag.getTag() == name:
                return tag
        return None

    def getType(self):
        return self.__class__

    def speechCommand(self):
        pass
