class Tag:
    def __init__(self, tag, value = None):
        self.tag = tag
        self.value = value

    def __str__(self):
        return ("Tag {}: {}".format(str(self.tag), str(self.value)))

    def __repr__(self):
        return ("({}: {})".format(str(self.tag), str(self.value)))

    def getTag(self):
        return self.tag

    def getValue(self):
        return self.value

    def setTag(self, tag):
        self.tag = tag

    def setValue(self, value):
        self.value = value
