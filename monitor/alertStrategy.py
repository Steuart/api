import askFor
import API

#告警策略
def alertStrategyPage():
    url = 'http://192.168.7.80:8080/manage/mobile/alertStrategy/paging'
    data = {
        "version":"hkv1",
        "start":0,
        "limit":15,
        "condition":"""{"name":""}"""
    }

    reData = askFor.post(url, data,jessionId="5C455DC9BA506BA746C44D148A4931F7")

    Page = API.Page
    page = Page()
    page.setH("==4.1 告警策略分页列表查询==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('告警策略分页列表查询')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/alertStrategyPage.md', 'w')
    f.write(data)
    f.close()
    print(data)

#添加告警策略
def addAlertStrategy():
    url = 'http://192.168.7.80:8080/manage/mobile/alertStrategy/save'
    data = {
        "version":"hkv1",
        "alertStrategy": """{
            "id": "",
            "created": "2014-4-11 16:46:18",
            "createdBy": "系统管理员",
            "updated": "",
            "updatedBy": "",
            "name": "测试",
            "oneLevelAlertTimes": "5",
            "oneLevelAlertInterval": "5",
            "twoLevelAlertTimes": "5",
            "twoLevelAlertInterval": "30",
            "threeLevelAlertTimes": "300",
            "threeLevelAlertInterval": "120"
        }"""
    }

    reData = askFor.post(url, data,jessionId="5C455DC9BA506BA746C44D148A4931F7")

    Page = API.Page
    page = Page()
    page.setH("==4.2 添加告警策略==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('添加告警策略')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/addAlertStrategy.md', 'w')
    f.write(data)
    f.close()
    print(data)

#修改告警策略
def modifyAlertStrategy():
    url = 'http://192.168.7.80:8080/manage/mobile/alertStrategy/save'
    data = {
        "version":"hkv1",
        "alertStrategy": """{
            "id": "2",
            "created": "2014-4-11 16:46:18",
            "createdBy": "系统管理员",
            "updated": "",
            "updatedBy": "",
            "name": "测试,测试",
            "oneLevelAlertTimes": "5",
            "oneLevelAlertInterval": "5",
            "twoLevelAlertTimes": "5",
            "twoLevelAlertInterval": "30",
            "threeLevelAlertTimes": "300",
            "threeLevelAlertInterval": "120"
        }"""
    }

    reData = askFor.post(url, data,jessionId="5C455DC9BA506BA746C44D148A4931F7")

    Page = API.Page
    page = Page()
    page.setH("==4.3 修改告警策略==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('修改告警策略')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/modifyAlertStrategy.md', 'w')
    f.write(data)
    f.close()
    print(data)

#禁用告警策略
def logicRemoveAlertStrategy():
    url = 'http://192.168.7.80:8080/manage/mobile/alertStrategy/logicRemove'
    data = {
        "version":"hkv1",
        "id":2
    }

    reData = askFor.post(url, data,jessionId="FD1807345BCB075B11B95C987B13483C")

    Page = API.Page
    page = Page()
    page.setH("==4.4 禁用告警策略==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('禁用告警策略')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/logicRemoveAlertStrategy.md', 'w')
    f.write(data)
    f.close()
    print(data)

#恢复告警策略
def recoveryAlertStrategy():
    url = 'http://192.168.7.80:8080/manage/mobile/alertStrategy/recovery'
    data = {
        "version":"hkv1",
        "id":2
    }

    reData = askFor.post(url, data,jessionId="FD1807345BCB075B11B95C987B13483C")

    Page = API.Page
    page = Page()
    page.setH("==4.5 恢复策略==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('恢复告警策略')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/recoveryAlertStrategy.md', 'w')
    f.write(data)
    f.close()
    print(data)

#获取告警策略详情
def getAlertStrategy():
    url = 'http://192.168.7.80:8080/manage/mobile/alertStrategy/get'
    data = {
        "version":"hkv1",
        "id":2
    }

    reData = askFor.post(url, data,jessionId="FD1807345BCB075B11B95C987B13483C")

    Page = API.Page
    page = Page()
    page.setH("==4.6 获取告警策略详情==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('获取告警策略详情')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/getAlertStrategy.md', 'w')
    f.write(data)
    f.close()
    print(data)

