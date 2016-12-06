
import API
import askFor

#监控插件分页列表
def page():
    url = 'http://192.168.7.80:8080/manage/mobile/program/paging'
    data = {
        "version":"hkv1",
        "start": 0,
        "limit": 15,
        "sort":"id",
        "dir":"DESC",
        "condition": {
            "name": "",
            "path": "",
            "businessGroup": "",
            "alertWay-eq": "",
            "alertTarget-eq": "",
            "servers": "",
            "createdBy-in": ""
        }
    }

    reData = askFor.post(url, data,jessionId="911CA8F87A5896AA23F6BB2F4028E41E")

    Page = API.Page
    page = Page()
    page.setH("==2.1 分页显示插件列表==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('分页显示插件列表')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/programPage.md', 'w')
    f.write(data)
    f.close()
    print(data)

#监控插件分页列表
def page2():
    url = 'http://192.168.7.80:8080/manage/mobile/program/paging'
    data = {
        "version":"hkv1",
        "start": 0,
        "limit": 15,
        "sort":"id",
        "dir":"DESC",
        "condition":{
        "name":"数据库定时备份插件",
        "path":"com.sw.dc.dw.monitor.platform.plugin.server.DatabaseBackupMP",
        "businessGroup":"test",
        "alertWay-eq":"2",
        "alertTarget-eq":"0",
        "servers":"",
        "createdBy-in":"系统管理员"
        }
    }

    reData = askFor.post(url, data,jessionId="911CA8F87A5896AA23F6BB2F4028E41E")

    Page = API.Page
    page = Page()
    page.setH("==2.1 分页显示插件列表==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('分页显示插件列表')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/programPage.md', 'w')
    f.write(data)
    f.close()
    print(data)



#监控插件详情
def pluginDetail():
    url = 'http://192.168.7.80:8080/manage/mobile/program/get'
    data = {
        "version": "hkv1",
        "id":4
    }

    reData = askFor.post(url, data, jessionId="D426365462A65AA4BBCC2D3C60C10DEE")

    Page = API.Page
    page = Page()
    page.setH("==2.2 监控插件详情==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('监控插件详情')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/programGet.md', 'w')
    f.write(data)
    f.close()
    print(data)

#保存修改监控插件
def save():
    url = 'http://192.168.0.2:8080/monitor/manage/mobile/program/save'
    data = {
        "version": "hkv1",
        "program":"""{
            "id":"9",
        "created":"2016-7-10 11:13:56",
        "createdBy":"系统管理员",
        "updated":"2016-10-08 09:55:15",
        "updatedBy":"系统管理员",
        "name":"服务器磁盘空间监控",
        "path":"com.sw.dc.dw.monitor.platform.plugin.server.ServerDiskSpaceMP",
        "parameters":"",
        "businessGroup":"",
        "startupHour":"",
        "startupMinute":"",
        "shutdownHour":"",
        "shutdownMinute":"",
        "interval":"5",
        "smsPlatform":"web",
        "smsSignature":"统一监控平台",
        "alertWay":"2",
        "alertTarget":"0",
        "servers":"",
        "serverUserId":"",
        "description":"",
        "ownerAlertStrategy":"1-1",
        "dutyManAlertStrategy":""
        }"""
    }

    reData = askFor.post(url, data, jessionId="D426365462A65AA4BBCC2D3C60C10DEE")
    print(reData)


#保存修改监控插件
def save1():
    url = 'http://192.168.0.2:8080/monitor/manage/mobile/program/save'
    data = {
        "version": "hkv1",
        "program":"""{
            "id": "2",
            "version": "hkv1",
            "shutdownMinute": "21",
            "startupHour": "2",
            "servers": "",
            "lastRunTime": "2016-09-22 07:30:40",
            "parameters": "Test123 ",
            "active": True,
            "businessGroup":"",
            "shutdownTime": "2016-10-25 10:21:00",
            "ownerAlertStrategy": "1-1",
            "alertWay": "2",
            "path": "com.sw.dc.dw.monitor.platform.plugin.server.DatabaseBackupMP",
            "shutdownHour": "10",
            "updated": "2016-10-25 15:06:19",
            "name": "数据库定时备份插件1111",
            "dutyManAlertStrategy": "",
            "createdBy": "系统管理员",
            "startupMinute": "5",
            "startupTime": "2016-10-25 02:05:00",
            "smsPlatform": "web",
            "smsSignature": "统一监控平台",
            "mailAlert": "0",
            "interval": "1200",
            "created": "2016-07-10 11:05:44",
            "smsAlert": "1"
        }"""
    }
    reData = askFor.post(url, data, jessionId="0F15968993FFBA5F8CE8E34F193F651D")
    print(reData)


def saveSqlProgeram():
    url = 'http://192.168.7.80:8080/manage/mobile/program/save'
    data = {
        "version": "hkv1",
        "program":"""{
        "id":"",
        "created":"2016-10-10 10:33:41",
        "createdBy":"系统管理员",
        "updated":"2016-10-10 10:33:41",
        "updatedBy":"系统管理员",
        "name":"sqltest",
        "path":"com.sw.dc.dw.monitor.platform.plugin.common.SQLMP",
        "parameters":"test",
        "businessGroup":"test",
        "startupHour":"02",
        "startupMinute":"03",
        "shutdownHour":"02",
        "shutdownMinute":"04",
        "interval":"",
        "smsPlatform":"web",
        "smsSignature":"统一监控平台",
        "alertWay":"2",
        "alertTarget":"0",
        "servers":"",
        "serverUserId":"",
        "description":"sql监控插件test",
        "monitorExpression":"select * from test",
        "jobId1":"",
        "dataSourceId1":"1",
        "monitorSql1":"select * from test",
        "jobId2":"",
        "dataSourceId2":"1",
        "monitorSql2":"select * from test",
        "jobId3":"",
        "dataSourceId3":"",
        "monitorSql3":"",
        "jobId4":"",
        "dataSourceId4":"",
        "monitorSql4":"",
        "jobId5":"",
        "dataSourceId5":"",
        "monitorSql5":"",
        "jobId6":"",
        "dataSourceId6":"",
        "monitorSql6":"",
        "messageTitle":"",
        "customSmsMessage":"",
        "customMailMessageType":"1",
        "customMailMessage":"",
        "ownerAlertStrategy":"1-2",
        "dutyManAlertStrategy":""
        }"""
    }


    reData = askFor.post(url, data, jessionId="911CA8F87A5896AA23F6BB2F4028E41E")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==2.4 修改sql监控插件==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('监控插件详情')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/programSqlSave.md', 'w')
    f.write(data)
    f.close()
    print(data)

def saveShellProgeram():
    url = 'http://192.168.7.80:8080/manage/mobile/program/save'
    data = {
        "version": "hkv1",
        "program":"""{
        "id":"18",
        "created":"2016-10-10 10:49:42",
        "createdBy":"系统管理员",
        "updated":"2016-10-10 10:49:42",
        "updatedBy":"系统管理员",
        "name":"shellTest",
        "path":"com.sw.dc.dw.monitor.platform.plugin.common.ShellMP",
        "parameters":"test",
        "businessGroup":"test",
        "startupHour":"03",
        "startupMinute":"06",
        "shutdownHour":"03",
        "shutdownMinute":"03",
        "interval":"12",
        "smsPlatform":"web",
        "smsSignature":"统一监控平台",
        "alertWay":"2",
        "alertTarget":"0",
        "servers":"2",
        "serverUserId":"2",
        "description":"test",
        "monitorShell":"ls -l",
        "monitorExpression":"",
        "monitorSuccessShell":"",
        "customMailMessageType":"1",
        "messageTitle":"test",
        "customSmsMessage":"test",
        "customMailMessage":"test",
        "ownerAlertStrategy":"3-1",
        "dutyManAlertStrategy":""
        }"""
    }


    reData = askFor.post(url, data, jessionId="911CA8F87A5896AA23F6BB2F4028E41E")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==2.5 修改shell监控插件==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('监控插件详情')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/programShellSave.md', 'w')
    f.write(data)
    f.close()
    print(data)

#删除监控插件配置
def remove():
    url = 'http://192.168.7.80:8080/manage/mobile/program/remove'
    data = {
        "version": "hkv1",
        "id": "11,12"
    }

    reData = askFor.post(url, data, jessionId="DFAF612E494709EC6028CBDA799E9A60")

    Page = API.Page
    page = Page()
    page.setH("==2.4 删除监控插件==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('删除监控插件')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/programDelete.md', 'w')
    f.write(data)
    f.close()
    print(data)

#禁用插件
def loginRemove():
    url = 'http://192.168.7.80:8080/manage/mobile/program/logicRemove'
    data = {
        "version": "hkv1",
        "id": 7
    }

    reData = askFor.post(url, data, jessionId="35B7F946FE8057AF524AD1707CC3A699")

    Page = API.Page
    page = Page()
    page.setH("==2.5 禁用监控插件==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('禁用监控插件')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/programLogicRm.md', 'w')
    f.write(data)
    f.close()
    print(data)

loginRemove()

#恢复插件为可用
def reCover():
    url = 'http://192.168.7.80:8080/manage/mobile/program/recovery'
    data = {
        "version": "hkv1",
        "id": 7
    }

    reData = askFor.post(url, data, jessionId="DFAF612E494709EC6028CBDA799E9A60")

    Page = API.Page
    page = Page()
    page.setH("==2.6 恢复插件为可用状态==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('恢复插件为可用状态')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/programRecover.md', 'w')
    f.write(data)
    f.close()
    print(data)

#查看执行日志
def checkLog():
    url = 'http://192.168.7.80:8080/manage/mobile/programLogger/log'
    data = {
        "version": "hkv1",
        "programId": 7
    }

    reData = askFor.post(url, data, jessionId="C7279B12BB6E772A111086007EC60680")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==2.7 查看执行日志==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('查看执行日志')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/programLog.md', 'w')
    f.write(data)
    f.close()
    print(data)

