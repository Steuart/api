import askFor
import API

#用户登录日志
def userLoginLog():
    url = 'http://192.168.7.80:8080/manage/mobile/loginLogger/paging'
    data = {
        "start":0,
        "limit":15,
        "sort":"id",
        "dir":"DESC",
        "condition":"""{"userId-eq":"","loginIp":"","created-ge":"","created-le":""}"""
    }

    reData = askFor.post(url, data,jessionId="07DA34EA459B8DE5C4CC041FE401BCEE")

    Page = API.Page
    page = Page()
    page.setH("==6.1 用户登录日志==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('用户登录日志列表')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/userLoginLog.md', 'w')
    f.write(data)
    f.close()
    print(data)

#用户操作日志
def operateLogger():
    url = 'http://192.168.7.80:8080/manage/mobile/operateLogger/paging'
    data = {
        "start":0,
        "limit":15,
        "sort":"id",
        "dir":"DESC",
        "condition":""""{"userId-eq":"","operateIp":"","operateAction-eq":"","created-ge":"","created-le":""}"""
    }

    reData = askFor.post(url, data,jessionId="07DA34EA459B8DE5C4CC041FE401BCEE")

    Page = API.Page
    page = Page()
    page.setH("==6.2 用户操作日志列表==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('用户操作日志列表')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/operateLogger.md', 'w')
    f.write(data)
    f.close()
    print(data)

#程序执行日志列表
def programLoggerPage():
    url = 'http://192.168.7.80:8080/manage/mobile/programLogger/paging'
    data = {
        "start":0,
        "limit":15,
        "sort":"id",
        "dir":"DESC",
        "condition":"""{"programName":"","status-in":"","logDate-ge":"","logDate-le":""}"""
    }

    reData = askFor.post(url, data,jessionId="07DA34EA459B8DE5C4CC041FE401BCEE")

    Page = API.Page
    page = Page()
    page.setH("==6.3 分页程序执行日志列表==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('程序执行日志列表')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/programLoggerPage.md', 'w')
    f.write(data)
    f.close()
    print(data)

#查看程序执行日志详情
def programLoggerDetail():
    url = 'http://192.168.7.80:8080/manage/mobile/programLogger/get'
    data = {
        "version":"hkv1",
        "id":15868,
    }

    reData = askFor.post(url, data,jessionId="3F752E8EA55E8EF14A7BBAA374024791")

    Page = API.Page
    page = Page()
    page.setH("==6.3 查看程序执行日志详情==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('查看程序执行日志详情')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/programLoggerDetail.md', 'w')
    f.write(data)
    f.close()
    print(data)
#删除程序执行日志
def programLoggerDelete():
    url = 'http://192.168.7.80:8080/manage/mobile/programLogger/remove'
    data = {
        "version":"hkv1",
        "id":15868,
    }

    reData = askFor.post(url, data,jessionId="3F752E8EA55E8EF14A7BBAA374024791")

    Page = API.Page
    page = Page()
    page.setH("==6.3 删除程序执行日志==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('删除程序执行日志')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/programLoggerDelete.md', 'w')
    f.write(data)
    f.close()
    print(data)

#查看程序执行日志
def programLogger():
    url = 'http://192.168.7.80:8080/manage/mobile/programLogger/log'
    data = {
        "version":"hkv1",
        "logPath":"/home/tools/logs/monitor/plugin/2016-09-23/03/ServerShutdownMP_31m26s.log"
    }

    reData = askFor.post(url, data,jessionId="07DA34EA459B8DE5C4CC041FE401BCEE")

    Page = API.Page
    page = Page()
    page.setH("==6.4 查看程序执行日志==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('查看程序执行日志')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/programLogger.md', 'w')
    f.write(data)
    f.close()
    print(data)

#程序告警日志分页列表
def alertLoggerPage():
    url = 'http://192.168.7.80:8080/manage/mobile/alertLogger/paging'
    data = {
        "version":"hkv1",
        "start":0,
        "limit":15,
        "sort":"id",
        "dir":"DESC",
        "condition":"""{"programName":"","alertDate-ge":"","alertDate-le":""}"""
    }

    reData = askFor.post(url, data,jessionId="3F752E8EA55E8EF14A7BBAA374024791")

    Page = API.Page
    page = Page()
    page.setH("==6.5 程序告警日志分页列表==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('程序告警日志分页列表')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/alertLoggerPage.md', 'w')
    f.write(data)
    f.close()
    print(data)

#程序告警日志分页详情
def alertLoggerDetail():
    url = 'http://192.168.7.80:8080/manage/mobile/alertLogger/get'
    data = {
        "version":"hkv1",
        "id":16
    }

    reData = askFor.post(url, data,jessionId="3F752E8EA55E8EF14A7BBAA374024791")

    Page = API.Page
    page = Page()
    page.setH("==6.6 程序告警日志详情==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('程序告警日志详情')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/alertLoggerDetail.md', 'w')
    f.write(data)
    f.close()
    print(data)

#分页查看程序告警状态列表
def programAlertStatusPage():
    url = 'http://192.168.7.80:8080/manage/mobile/programAlertStatus/paging'
    data = {
        "version": "hkv1",
        "start":0,
        "limit":15,
        "sort":"id",
        "dir":"DESC",
        "condition":"""{"programName":"","userName":"","alertDate-ge":"","alertDate-le":""}"""
    }

    reData = askFor.post(url, data, jessionId="07DA34EA459B8DE5C4CC041FE401BCEE")

    Page = API.Page
    page = Page()
    page.setH("==6.5 分页查看程序告警状态列表==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('分页查看程序告警状态列表')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/programAlertStatusPage.md', 'w')
    f.write(data)
    f.close()
    print(data)

#程序告警日志详情
def programAlertStatusDetail():
    url = 'http://192.168.7.80:8080/manage/mobile/alertLogger/get'
    data = {
        "version": "hkv1",
        "id":28
    }

    reData = askFor.post(url, data, jessionId="07DA34EA459B8DE5C4CC041FE401BCEE")

    Page = API.Page
    page = Page()
    page.setH("==6.6 程序告警日志详情==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('程序告警日志详情')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/programAlertDetail.md', 'w')
    f.write(data)
    f.close()
    print(data)
programAlertStatusDetail()

#获取程序告警状态详情
def getProgramAlertStatus():
    url = 'http://192.168.7.80:8080/manage/mobile/programAlertStatus/get'
    data = {
        "version": "hkv1",
        "id":7
    }

    reData = askFor.post(url, data, jessionId="9EC8B5E9A293BFB3FB06DB8C989B98EA")

    Page = API.Page
    page = Page()
    page.setH("==6.6 查看程序告警状态详情==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('查看程序告警状态详情')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/getProgramAlertStatus.md', 'w')
    f.write(data)
    f.close()
    print(data)
getProgramAlertStatus()

#删除程序告警状态
def removeProgramAlertStatus():
    url = 'http://192.168.7.80:8080/manage/mobile/programAlertStatus/remove'
    data = {
        "version": "hkv1",
        "id":1
    }

    reData = askFor.post(url, data, jessionId="3F752E8EA55E8EF14A7BBAA374024791")

    Page = API.Page
    page = Page()
    page.setH("==6.7 删除程序告警状态详情==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('删除程序告警状态详情')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/removeProgramAlertStatus.md', 'w')
    f.write(data)
    f.close()
    print(data)