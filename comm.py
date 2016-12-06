

class DictHandler:
    def __init__(self):
        "dict帮助类"
        self.map = {}
    #解析map所有的键值
    def getKeys(self,data):
        if(type(data) == type("")):
            return
        for (key, value) in data.items():
            self.map[key]=str(type(value)).split("'")[1]
            if (type(value) == type("") or type(value) == type(0)):
                continue
            #数组的情况
            elif(type(value) == type([]) and len(value) !=0):
                if (type(data[key][0]) == type(0)):
                    return
                self.getKeys(data[key][0])
            #字典的情况
            elif(type(value) == type({})):
                self.getKeys(data[key])
        return self.map;

