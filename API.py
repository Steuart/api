import comm
import json
class Page:
    """api markdown页面"""
    def __init__(self):
        #标题
        self.h = ''
        #简要描述
        self.scribe = ''
        #请求url
        self.url = ''
        #请求方式
        self.method = ''
        #参数
        self.reqParams = ''
        #请求示例
        self.reqEx = ''
        #返回示例
        self.resEx = ''
        #返回参数说明
        self.resParams = ''

    #设置标题
    def setH(self,content,level):
        number = ''
        for i in range(level):
            number +='#'
        self.h = number + content +'\n'

    #设置简要描述
    def setScribe(self,content):
        self.scribe= "- " + content + '\n'

    #设置url内容
    def setUrl(self,content):
        self.url = '- ```' + json.dumps(content,indent=4) + '```\n'

    #设置请求类型
    def setMethod(self,content):
        self.method = "- " + content + "\n"

    #设置参数描述
    def setReqParams(self,content):

        #如果参数长度是零，则为无参数
        if(len(content)==0):
            self.reqParams = "- 无参数 \n\n"
            return

        str = "|参数名|必选|类型|说明|\n" \
              "| :---------- | :--- | :----- | -------- |\n"
        dictHandler = comm.DictHandler()
        keys = dictHandler.getKeys(content)
        for key in keys:
            str += "|"+key+"| |"+keys[key]+"| |\n"
        self.reqParams = str

    #设置参数示例
    def setReqEx(self,content):

        # 如果参数长度是零，则为无参数
        if (len(content) == 0):
            self.reqEx = "- 无参数 \n\n"
            return

        self.reqEx = '```\n' + json.dumps(content,indent=4,ensure_ascii=False) + '\n```\n'

    #设置返回示例
    def setResEx(self,content):
        self.resEx = '```\n' + json.dumps(json.loads(content),indent=4,ensure_ascii=False) + '\n```\n'

    #设置返回参数说明
    def setResParams(self,content):
        content = json.loads(content)
        str = "|参数名|类型|说明|\n" \
              "|:---|:---|:---|\n"
        dictHandler = comm.DictHandler()
        keys = dictHandler.getKeys(content)

        for key in keys:
            str += "|" + key + "|" + keys[key] + "| |\n"
        self.resParams = str

    def getPage(self):
        self.page = self.h+\
                    '\n**简要描述:**\n'+self.scribe+\
                    '\n**请求url:**\n' + self.url+\
                    '\n**请求方式:**\n' +self.method+\
                    '\n**参数说明:**\n' +self.reqParams+\
                    '\n**请求示例:**\n' +self.reqEx+\
                    '\n**返回示例:**\n' +self.resEx+\
                    '\n**返回参数说明:**\n'+self.resParams
        return self.page