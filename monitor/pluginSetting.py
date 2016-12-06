#插件配置
import API
import askFor

#服务器进程配置
def serverProcess():
    url = 'http://192.168.7.80:8080/manage/mobile/serverProcessMPC/paging'
    data = {
        "version": "hkv1",
        "start":0,
        "limit":15,
        "sort":"id",
        "dir":"DESC",
        "condition":{"serverId-eq":"","serverUserId-eq":""}
    }

    reData = askFor.post(url, data, jessionId="C7279B12BB6E772A111086007EC60680")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.1 服务器进程配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('服务器进程配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/serverProcess.md', 'w')
    f.write(data)
    f.close()
    print(data)

#添加服务器进程
def addServerProcess():
    url = 'http://192.168.7.80:8080/manage/mobile/serverProcessMPC/save'
    data = {
        "version": "hkv1",
        "serverProcessMPC":"""{"id":"","created":"2016-10-08 11:30:50","createdBy":"系统管理员","updated":"2016-10-08 11:30:50","updatedBy":"系统管理员","serverId":"1","serverUserId":"1","process":"aaaa","startupCommand":"aaaa","description":"这是一个测试"}"""
    }

    reData = askFor.post(url, data, jessionId="C7279B12BB6E772A111086007EC60680")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.2 添加服务器进程配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('添加服务器进程配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/addServerProcess.md', 'w')
    f.write(data)
    f.close()
    print(data)
#禁用服务器进程配置
def loginRemoveServerProcess():
    url = 'http://192.168.7.80:8080/manage/mobile/serverProcessMPC/logicRemove'
    data = {
        "version": "hkv1",
        "id": 2
    }

    reData = askFor.post(url, data, jessionId="9542D52913FC0A46A4BDFB59132EEA4B")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.3 禁用服务器进程配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('禁用服务器进程配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/logicRemoveServerProcess.md', 'w')
    f.write(data)
    f.close()
    print(data)

#恢复服务器进程配置
def recoverServerProcess():
    url = 'http://192.168.7.80:8080/manage/mobile/serverProcessMPC/recovery'
    data = {
        "version": "hkv1",
        "id": 2
    }

    reData = askFor.post(url, data, jessionId="9542D52913FC0A46A4BDFB59132EEA4B")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.4 恢复服务器进程配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('恢复服务器进程配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/recoverServerProcess.md', 'w')
    f.write(data)
    f.close()
    print(data)

#查看服务器进程配置
def detailServerProcess():
    url = 'http://192.168.7.80:8080/manage/mobile/serverProcessMPC/get'
    data = {
        "version": "hkv1",
        "id": 2
    }

    reData = askFor.post(url, data, jessionId="9542D52913FC0A46A4BDFB59132EEA4B")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.5 查看服务器进程配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('查看服务器进程配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/DetailServerProcess.md', 'w')
    f.write(data)
    f.close()
    print(data)

#编辑服务器进程配置
def editServerProcess():
    url = 'http://192.168.7.80:8080/manage/mobile/serverProcessMPC/save'
    data = {
        "version": "hkv1",
        "serverProcessMPC":"""{
        "id":"5",
        "created":"2016-6-23 13:22:03",
        "createdBy":"系统管理员",
        "updated":"2016-9-10 10:46:43",
        "updatedBy":"系统管理员",
        "serverId":"5",
        "serverUserId":"1",
        "process":"DataNode,NodeManager,HRegionServer,tomcat",
        "startupCommand":"",
        "description":"这是一个测试"
        }"""
    }

    reData = askFor.post(url, data, jessionId="9542D52913FC0A46A4BDFB59132EEA4B")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.6 编辑保存服务器进程配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('编辑保存服务器进程配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/editSaveServerProcess.md', 'w')
    f.write(data)
    f.close()
    print(data)


#服务器端口配置
def serverPort():
    url = 'http://192.168.7.80:8080/manage/mobile/serverPortMPC/paging'
    data = {
        "version": "hkv1",
        "start": 0,
        "limit": 15,
        "sort": "id",
        "dir": "DESC",
        "condition": {"serverId-eq": "", "serverUserId-eq": ""}
    }

    reData = askFor.post(url, data, jessionId="C7279B12BB6E772A111086007EC60680")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.2 服务器端口配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('服务器端口配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/serverPort.md', 'w')
    f.write(data)
    f.close()
    print(data)

#添加服务器端口配置
def addServerPort():
    url = 'http://192.168.7.80:8080/manage/mobile/serverPortMPC/save'
    data = {
        "version": "hkv1",
        "serverPortMPC": """{
            "id": "",
            "created": "2016-10-08 14:44:47",
            "createdBy": "系统管理员",
            "updated": "2016-10-08 14:44:47",
            "updatedBy": "系统管理员",
            "serverId": "1",
            "serverUserId": "1",
            "port": "3000",
            "startupCommand": "aaa",
            "description": "这是一个测试"
        }"""
    }

    reData = askFor.post(url, data, jessionId="C7279B12BB6E772A111086007EC60680")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.8 服务器端口配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('服务器端口配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/addServerPort.md', 'w')
    f.write(data)
    f.close()
    print(data)

#修改服务器端口配置
def modifyServerPort():
    url = 'http://192.168.7.80:8080/manage/mobile/serverPortMPC/save'
    data = {
        "version": "hkv1",
        "serverPortMPC":"""{
        "id":"2",
        "created":"2016-10-8 11:25:39",
        "createdBy":"系统管理员",
        "updated":"2016-10-8 14:56:22",
        "updatedBy":"系统管理员",
        "serverId":"2",
        "serverUserId":"1",
        "port":"8080",
        "startupCommand":"start",
        "description":"这是另外一个测试,测试，测试"
    }"""
    }

    reData = askFor.post(url, data, jessionId="C7279B12BB6E772A111086007EC60680")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.10 修改服务器端口配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('修改服务器端口配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/modifyServerPort.md', 'w')
    f.write(data)
    f.close()
    print(data)

#查看服务器端口配置
def detailServerPort():
    url = 'http://192.168.7.80:8080/manage/mobile/serverPortMPC/save'
    data = {
        "version": "hkv1",
        "id": 2
    }

    reData = askFor.post(url, data, jessionId="C7279B12BB6E772A111086007EC60680")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.9 查看服务器端口配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('查看服务器端口配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/detailServerPort.md', 'w')
    f.write(data)
    f.close()
    print(data)

#禁用服务器端口配置
def disableServerPort():
    url = 'http://192.168.7.80:8080/manage/mobile/serverPortMPC/logicRemove'
    data = {
        "version": "hkv1",
        "id": 2
    }

    reData = askFor.post(url, data, jessionId="C5CA09AA9185FFFADDCBBF26A129C436")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.11 禁用服务器端口配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('禁用服务器端口配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/disableServerPort.md', 'w')
    f.write(data)
    f.close()
    print(data)

#恢复服务器端口配置
def recoverServerPort():
    url = 'http://192.168.7.80:8080/manage/mobile/serverPortMPC/recovery'
    data = {
        "version": "hkv1",
        "id": 2
    }

    reData = askFor.post(url, data, jessionId="C5CA09AA9185FFFADDCBBF26A129C436")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.12 恢复服务器端口配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('恢复服务器端口配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/recoverServerPort.md', 'w')
    f.write(data)
    f.close()
    print(data)

#kerberos证书配置分页列表
def certificateUserPage():
    url = 'http://192.168.7.80:8080/manage/mobile/certificateUserMPC/paging'
    data = {
        "version":"hkv1",
        "start":0,
        "limit":15,
        "sort":"id",
        "dir":"DESC",
        "condition":"""{"serverId-eq":"","serverUserId-eq":""}"""
    }

    reData = askFor.post(url, data, jessionId="C5CA09AA9185FFFADDCBBF26A129C436")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.13 kerberos证书用户配置分页列表==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('kerberos证书用户配置分页列表')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/kerberosPage.md', 'w')
    f.write(data)
    f.close()
    print(data)

def addCertificateUser():
    url = 'http://192.168.7.80:8080/manage/mobile/certificateUserMPC/save'
    data = {
        "version": "hkv1",
        "certificateUserMPC": """{
                "id":"",
                "created":"2016-10-8 11:24:14",
                "createdBy":"系统管理员",
                "updated":"2016-10-8 11:23:58",
                "updatedBy":"系统管理员",
                "serverId":"2",
                "serverUserId":"1",
                "certificateUsername":"系统管理员",
                "description":"这是另外一个测试"
            }"""
    }

    reData = askFor.post(url, data, jessionId="C5CA09AA9185FFFADDCBBF26A129C436")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.14 添加kerberos证书用户配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('添加kerberos证书用户配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/addKerberos.md', 'w')
    f.write(data)
    f.close()
    print(data)

#修改kerberos证书用户配置
def modifyCertificateUser():
    url = 'http://192.168.7.80:8080/manage/mobile/certificateUserMPC/save'
    data = {
        "version": "hkv1",
        "certificateUserMPC": """{
                "id":"2",
                "created":"2016-10-8 11:24:14",
                "createdBy":"系统管理员",
                "updated":"2016-10-8 11:23:58",
                "updatedBy":"系统管理员",
                "serverId":"2",
                "serverUserId":"1",
                "certificateUsername":"系统管理员",
                "description":"这是另外一个测试,测试，测试"
            }"""
    }

    reData = askFor.post(url, data, jessionId="C5CA09AA9185FFFADDCBBF26A129C436")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.15 修改kerberos证书用户配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('修改kerberos证书用户配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/modifyKerberos.md', 'w')
    f.write(data)
    f.close()
    print(data)

#禁用kerberos证书用户配置
def disableCertificateUser():
    url = 'http://192.168.7.80:8080/manage/mobile/certificateUserMPC/logicRemove'
    data = {
        "version": "hkv1",
        "id": 2
    }

    reData = askFor.post(url, data, jessionId="C5CA09AA9185FFFADDCBBF26A129C436")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.16 禁用kerberos证书用户配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('禁用kerberos证书配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/disableCertificateUser.md', 'w')
    f.write(data)
    f.close()
    print(data)


#恢复kerberos证书用户配置
def recoveryCertificateUser():
    url = 'http://192.168.7.80:8080/manage/mobile/certificateUserMPC/recovery'
    data = {
        "version": "hkv1",
        "id": 2
    }

    reData = askFor.post(url, data, jessionId="C5CA09AA9185FFFADDCBBF26A129C436")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.17 恢复kerberos证书用户配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('恢复kerberos证书配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/recoveryCertificateUser.md', 'w')
    f.write(data)
    f.close()
    print(data)

#获取kerberos证书用户信息
def getCertificateUser():
    url = 'http://192.168.7.80:8080/manage/mobile/certificateUserMPC/get'
    data = {
        "version": "hkv1",
        "id": 2
    }

    reData = askFor.post(url, data, jessionId="C5CA09AA9185FFFADDCBBF26A129C436")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.18 获取kerberos证书用户配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('获取kerberos证书配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/getCertificateUser.md', 'w')
    f.write(data)
    f.close()
    print(data)


#服务器备份数据库配置分页列表
def serverDatabasePage():
    url = 'http://192.168.7.80:8080/manage/mobile/serverDatabaseMPC/paging'
    data = {
        "version":"hkv1",
        "start":0,
        "limit":15,
        "sort":"id",
        "dir":"DESC",
        "condition":{"serverId-eq":"","serverUserId-eq":""}
    }

    reData = askFor.post(url, data, jessionId="911CA8F87A5896AA23F6BB2F4028E41E")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.19 服务器备份数据库配置分页列表==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('服务器备份数据库配置分页列表')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/serverDatabasePage.md', 'w')
    f.write(data)
    f.close()
    print(data)

#获取服务器备份数据库配置
def getDatabase():
    url = 'http://192.168.7.80:8080/manage/mobile/serverDatabaseMPC/get'
    data = {
        "version": "hkv1",
        "id": 1
    }

    reData = askFor.post(url, data, jessionId="C5CA09AA9185FFFADDCBBF26A129C436")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.20 获取服务器备份数据库配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('获取服务器备份数据库配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/getDatabase.md', 'w')
    f.write(data)
    f.close()
    print(data)

#添加服务器备份数据配置
def addDatabase():
    url = 'http://192.168.7.80:8080/manage/mobile/serverDatabaseMPC/save'
    data = {
        "version": "hkv1",
        "serverDatabaseMPC":"""{
            "id":"",
            "created":"2016-7-10 11:04:58",
            "createdBy":"系统管理员",
            "updated":"2016-10-8 15:43:06",
            "updatedBy":"系统管理员",
            "serverId":"4",
            "serverUserId":"1",
            "username":"root",
            "password":"123456a",
            "port":"3306",
            "database":"etl,hive,metadata,monitor_platform,odps,scheduler,spider,spider_result",
            "description":""
        }"""
    }

    reData = askFor.post(url, data, jessionId="C5CA09AA9185FFFADDCBBF26A129C436")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.21 添加备份数据库配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe("添加备份数据库配置")
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/addDatabase.md', 'w')
    f.write(data)
    f.close()
    print(data)

#修改服务器备份数据库配置
def modifyDatabase():
    url = 'http://192.168.7.80:8080/manage/mobile/serverDatabaseMPC/save'
    data = {
        "version": "hkv1",
        "serverDatabaseMPC": """{
                "id":"1",
                "created":"2016-7-10 11:04:58",
                "createdBy":"系统管理员",
                "updated":"2016-10-8 15:43:06",
                "updatedBy":"系统管理员",
                "serverId":"5",
                "serverUserId":"1",
                "username":"root",
                "password":"123456a",
                "port":"3306",
                "database":"etl,hive,metadata,monitor_platform,odps,scheduler,spider,spider_result",
                "description":"这是一个测试"
            }"""
    }

    reData = askFor.post(url, data, jessionId="C5CA09AA9185FFFADDCBBF26A129C436")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.22 修改备份数据库配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe("修改备份数据库配置")
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/modifyDatabase.md', 'w')
    f.write(data)
    f.close()
    print(data)

#禁用数据库备份配置
def disableDatabase():
    url = 'http://192.168.7.80:8080/manage/mobile/serverDatabaseMPC/logicRemove'
    data = {
        "version": "hkv1",
        "id": 2
    }

    reData = askFor.post(url, data, jessionId="ED3432EE477433FDC9B56DB9375B1893")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.23 禁用服务器备份数据库配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('禁用服务器备份数据库配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/logicRemoceDatabase.md', 'w')
    f.write(data)
    f.close()
    print(data)

#恢复数据库备份配置
def revoceryDatabase():
    url = 'http://192.168.7.80:8080/manage/mobile/serverDatabaseMPC/recovery'
    data = {
        "version": "hkv1",
        "id": 2
    }

    reData = askFor.post(url, data, jessionId="ED3432EE477433FDC9B56DB9375B1893")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.23 禁用服务器备份数据库配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('禁用服务器备份数据库配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/recoveryDatabase.md', 'w')
    f.write(data)
    f.close()
    print(data)

#修改服务器备份数据库密码
def modifyDatabasePassword():
    url = 'http://192.168.7.80:8080/manage/mobile/serverDatabaseMPC/password'
    data = {
        "version": "hkv1",
        "serverDatabaseMPCId":2,
        "password":"123456a"
    }

    reData = askFor.post(url, data, jessionId="2D4017FF7B9AC02B552BADEC5AD34A21")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.25 修改服务器备份数据库密码==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('修改服务器备份数据库密码')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/modifyDatabasePassword.md', 'w')
    f.write(data)
    f.close()
    print(data)

#磁盘空间策略列表
def diskSpacePage():
    url = 'http://192.168.7.80:8080/manage/mobile/diskSpaceStrategy/paging'
    data = {
        "version": "hkv1",
        "start":0,
        "limit":15,
        "sort":"id",
        "dir":"DESC",
        "condition":"""{"name":""}"""
    }

    reData = askFor.post(url, data, jessionId="2D4017FF7B9AC02B552BADEC5AD34A21")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.26 磁盘空间分页列表==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('磁盘空间策略分页列表')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/diskSpaceStrategy.md', 'w')
    f.write(data)
    f.close()
    print(data)

#添加磁盘空间策略
def addDiskSpace():
    url = 'http://192.168.7.80:8080/manage/mobile/diskSpaceStrategy/save'
    data = {
        "version": "hkv1",
        "diskSpaceStrategy":"""{
        "id":"",
        "created":"2016-10-08 16:26:09",
        "createdBy":"系统管理员",
        "updated":"2016-10-08 16:26:09",
        "updatedBy":"系统管理员",
        "name":"test",
        "description":"这是一个测试",
        "startWeek1":"2",
        "endWeek1":"2",
        "startTime1":"00:00",
        "endTime1":"00:00",
        "percent1":"70",
        "startWeek2":"3",
        "endWeek2":"3",
        "startTime2":"01:30",
        "endTime2":"05:00",
        "percent2":"10",
        "startWeek3":"5",
        "endWeek3":"1",
        "startTime3":"05:30",
        "endTime3":"06:30",
        "percent3":"10"
         }"""
    }

    reData = askFor.post(url, data, jessionId="2D4017FF7B9AC02B552BADEC5AD34A21")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.27 添加磁盘空间策略==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('添加磁盘空间策略')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/addDiskSpace.md', 'w')
    f.write(data)
    f.close()
    print(data)

#删除磁盘空间策略
def deleteDiskSpace():
    url = 'http://192.168.7.80:8080/manage/mobile/diskSpaceStrategy/remove'
    data = {
        "version": "hkv1",
        "id":2
    }

    reData = askFor.post(url, data, jessionId="6B50FAB455BFE207DDC65CD6AEA082DB")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.28 删除磁盘空间策略==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('删除磁盘空间策略')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/removeDiskSpace.md', 'w')
    f.write(data)
    f.close()
    print(data)

#获取磁盘空间策略
def getDisSpace():
    url = 'http://192.168.7.80:8080/manage/mobile/diskSpaceStrategy/get'
    data = {
        "version": "hkv1",
        "id": 3
    }

    reData = askFor.post(url, data, jessionId="6B50FAB455BFE207DDC65CD6AEA082DB")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.29 获取磁盘空间策略==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('获取磁盘空间策略')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/getDiskSpace.md', 'w')
    f.write(data)
    f.close()
    print(data)

#修改磁盘空间策略
def modifyDiskSpace():
    url = 'http://192.168.7.80:8080/manage/mobile/diskSpaceStrategy/save'
    data = {
        "version": "hkv1",
        "diskSpaceStrategy":"""{
        "id":"3",
        "created":"2016-10-08 16:26:09",
        "createdBy":"系统管理员",
        "updated":"2016-10-08 16:26:09",
        "updatedBy":"系统管理员",
        "name":"test",
        "description":"这是一个测试,测试",
        "startWeek1":"2",
        "endWeek1":"2",
        "startTime1":"00:00",
        "endTime1":"00:00",
        "percent1":"70",
        "startWeek2":"3",
        "endWeek2":"3",
        "startTime2":"01:30",
        "endTime2":"05:00",
        "percent2":"10",
        "startWeek3":"5",
        "endWeek3":"1",
        "startTime3":"05:30",
        "endTime3":"06:30",
        "percent3":"10"
         }"""
    }

    reData = askFor.post(url, data, jessionId="6B50FAB455BFE207DDC65CD6AEA082DB")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.30 修改磁盘空间策略==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('修改磁盘空间策略')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/modifyDiskSpace.md', 'w')
    f.write(data)
    f.close()
    print(data)

#禁用磁盘空间策略
def DisSpaceLoginRemove():
    url = 'http://192.168.7.80:8080/manage/mobile/diskSpaceStrategy/logicRemove'
    data = {
        "version": "hkv1",
        "id": 3
    }

    reData = askFor.post(url, data, jessionId="6B50FAB455BFE207DDC65CD6AEA082DB")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.29 获取磁盘空间策略==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('获取磁盘空间策略')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/diskSpaceLogicRemove.md', 'w')
    f.write(data)
    f.close()
    print(data)

#恢复磁盘空间策略
def disSpaceRecovery():
    url = 'http://192.168.7.80:8080/manage/mobile/diskSpaceStrategy/recovery'
    data = {
        "version": "hkv1",
        "id": 3
    }

    reData = askFor.post(url, data, jessionId="6B50FAB455BFE207DDC65CD6AEA082DB")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.29 获取磁盘空间策略==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('获取磁盘空间策略')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/diskSpaceRecovery.md', 'w')
    f.write(data)
    f.close()
    print(data)



#服务器磁盘空间配置

def serverDiskSpace():
    url = 'http://192.168.7.80:8080/manage/mobile/serverDiskSpaceMPC/paging'
    data = {
        "version": "hkv1",
        "start": 0,
        "limit": 15,
        "sort": "id",
        "dir": "DESC",
        "condition":"""{"serverId-eq":"","serverUserId-eq":""}"""
    }

    reData = askFor.post(url, data, jessionId="2D4017FF7B9AC02B552BADEC5AD34A21")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.31 服务器磁盘空间配置列表==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('服务器磁盘空间配置列表')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/serverDiskSpace.md', 'w')
    f.write(data)
    f.close()
    print(data)

#添加服务器磁盘空间策略
def addServerDisk():
    url = 'http://192.168.0.2:8080/monitor/manage/mobile/serverDiskSpaceMPC/save'
    #url = 'http://192.168.7.80:8080/manage/mobile/serverDiskSpaceMPC/save'
    data = {
        "version": "hkv1",
        "serverDiskSpaceMPC":"""{
        "id":"1",
        "created":"2016-10-08 16:45:36",
        "createdBy":"系统管理员",
        "updated":"2016-10-08 16:45:36",
        "updatedBy":"系统管理员",
        "serverId":"2",
        "serverUserId":"1",
        "diskSpaceStrategyId":"3",
        "description":"这是另外一个测试,长长长长长长长长"
        }"""
    }

    reData = askFor.post(url, data, jessionId="2504AD43C332F1D607ADC8A7A8700E20")
    #print(reData)
    #Page = API.Page
    #page = Page()
    #page.setH("==3.32 添加服务器磁盘空间配置==", 3)
    #page.setMethod('post')
    #page.setUrl(url)
    #page.setScribe('添加服务器磁盘空间配置列表')
    #page.setReqParams(data)
    #page.setReqEx(data)
    #page.setResEx(reData)
    #page.setResParams(reData)
    #data = page.getPage()
    #f = open('e:/api/addServerDisk.md', 'w')
    #f.write(data)
    #f.close()
    print(data)
#修改服务器磁盘空间策略
def modifyServerDisk():
    url = 'http://192.168.7.80:8080/manage/mobile/serverDiskSpaceMPC/save'
    data = {
        "version": "hkv1",
        "serverDiskSpaceMPC":"""{
        "id":"7",
        "created":"2016-10-08 16:45:36",
        "createdBy":"系统管理员",
        "updated":"2016-10-08 16:45:36",
        "updatedBy":"系统管理员",
        "serverId":"2",
        "serverUserId":"1",
        "diskSpaceStrategyId":"3",
        "description":"这是另外一个测试,测试，测试"
        }"""
    }

    reData = askFor.post(url, data, jessionId="E095C98CCA90507DCA3DF285E677F766")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.33 修改服务器磁盘空间配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('修改服务器磁盘空间配置列表')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/modifyServerDisk.md', 'w')
    f.write(data)
    f.close()
    print(data)

#获取服务器磁盘空间策略
def getServerDisk():
    url = 'http://192.168.7.80:8080/manage/mobile/serverDiskSpaceMPC/get'
    data = {
        "version": "hkv1",
        "id":"7"
    }
    reData = askFor.post(url, data, jessionId="E095C98CCA90507DCA3DF285E677F766")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.34 获取服务器磁盘空间配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('获取服务器磁盘空间配置列表')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/getServerDisk.md', 'w')
    f.write(data)
    f.close()
    print(data)

#禁用服务器磁盘空间策略
def logicRemoveServerDisk():
    url = 'http://192.168.7.80:8080/manage/mobile/serverDiskSpaceMPC/logicRemove'
    data = {
        "version": "hkv1",
        "id":"7"
    }
    reData = askFor.post(url, data, jessionId="E095C98CCA90507DCA3DF285E677F766")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.35 禁用服务器磁盘空间配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('禁用服务器磁盘空间配置列表')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/logicRemoveServerDisk.md', 'w')
    f.write(data)
    f.close()
    print(data)

#恢复服务器磁盘空间策略
def logicRemoveServerDisk():
    url = 'http://192.168.7.80:8080/manage/mobile/serverDiskSpaceMPC/recovery'
    data = {
        "version": "hkv1",
        "id":"7"
    }
    reData = askFor.post(url, data, jessionId="E095C98CCA90507DCA3DF285E677F766")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.36 恢复服务器磁盘空间配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('恢复服务器磁盘空间配置列表')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/logicRemoveServerDisk.md', 'w')
    f.write(data)
    f.close()
    print(data)

#服务器内存配置列表
def serverMemoryPage():
    url = 'http://192.168.7.80:8080/manage/mobile/serverMemoryMPC/paging'
    data = {
        "version":"hkv1",
        "start":0,
        "limit":15,
        "sort":"id",
        "dir":"DESC",
        "condition":"""{"serverId-eq":"","serverUserId-eq":""}"""
    }
    reData = askFor.post(url, data, jessionId="E095C98CCA90507DCA3DF285E677F766")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.37 服务器内存配置分页列表==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('服务器内存配置分页列表')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/serverMemoryPage.md', 'w')
    f.write(data)
    f.close()
    print(data)


#添加服务器内存配置
def addServerMemory():
    url = 'http://192.168.7.80:8080/manage/mobile/serverMemoryMPC/save'
    data = {
        "version":"hkv1",
        "serverMemoryMPC":"""{
        "id":"",
        "created":"2016-10-09 09:09:40",
        "createdBy":"系统管理员",
        "updated":"2016-10-09 09:09:40",
        "updatedBy":"系统管理员",
        "serverId":"2",
        "serverUserId":"1",
        "memoryThreshold":"10",
        "cumulativeCached":"true",
        "description":"这是一个测试"
        }"""
    }
    reData = askFor.post(url, data, jessionId="E095C98CCA90507DCA3DF285E677F766")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.38 添加服务器内存配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('添加服务器内存配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/addServerMemory.md', 'w')
    f.write(data)
    f.close()
    print(data)

#修改服务器内存配置
def modifyServerMemory():
    url = 'http://192.168.7.80:8080/manage/mobile/serverMemoryMPC/save'
    data = {
        "version":"hkv1",
        "serverMemoryMPC":"""{
        "id":"2",
        "created":"2016-10-09 09:09:40",
        "createdBy":"系统管理员",
        "updated":"2016-10-09 09:09:40",
        "updatedBy":"系统管理员",
        "serverId":"2",
        "serverUserId":"1",
        "memoryThreshold":"10",
        "cumulativeCached":"true",
        "description":"这是一个测试，测试"
        }"""
    }
    reData = askFor.post(url, data, jessionId="E095C98CCA90507DCA3DF285E677F766")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.39 修改服务器内存配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('修改服务器内存配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/modifyServerMemory.md', 'w')
    f.write(data)
    f.close()
    print(data)

#禁用服务器内存配置
def logicRemoveServerMemory():
    url = 'http://192.168.7.80:8080/manage/mobile/serverMemoryMPC/logicRemove'
    data = {
        "version":"hkv1",
        "id":1
    }
    reData = askFor.post(url, data, jessionId="E095C98CCA90507DCA3DF285E677F766")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.40 禁用服务器内存配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('禁用服务器内存配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/logicRemoveServerMemory.md', 'w')
    f.write(data)
    f.close()
    print(data)


#恢复服务器内存配置
def recoveryServerMemory():
    url = 'http://192.168.7.80:8080/manage/mobile/serverMemoryMPC/recovery'
    data = {
        "version":"hkv1",
        "id":1
    }
    reData = askFor.post(url, data, jessionId="E095C98CCA90507DCA3DF285E677F766")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.41 恢复服务器内存配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('恢复服务器内存配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/recoveryServerMemory.md', 'w')
    f.write(data)
    f.close()
    print(data)

#获取服务器内存配置
def getServerMemory():
    url = 'http://192.168.7.80:8080/manage/mobile/serverMemoryMPC/get'
    data = {
        "version": "hkv1",
        "id": 1
    }
    reData = askFor.post(url, data, jessionId="E095C98CCA90507DCA3DF285E677F766")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.41 获取服务器内存配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('获取服务器内存配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/getServerMemory.md', 'w')
    f.write(data)
    f.close()
    print(data)

#hadoop集群监控指标配置
def hadoopMPCPage():
    url = 'http://192.168.7.80:8080/manage/mobile/hadoopMPC/paging'
    data = {
        "start":0,
        "limit":15,
        "sort":"id",
        "dir":"DESC",
        "condition": """{}"""
    }
    reData = askFor.post(url, data, jessionId="E095C98CCA90507DCA3DF285E677F766")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.43 获取hadoop集群监控指标配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('获取服务器内存配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/hadoopMPCPage.md', 'w')
    f.write(data)
    f.close()
    print(data)

#添加hadoop集群监控指标配置
def addHadoopMPC():
    url = 'http://192.168.7.80:8080/manage/mobile/hadoopMPC/save'
    data = {
        "version":"hkv1",
        "hadoopMPC":"""{
        "id":"",
        "created":"2014-4-6 18:49:08",
        "createdBy":"系统管理员",
        "updated":"",
        "updatedBy":"",
        "taskTrackerNumber":"13",
        "datanodeNumber":"13",
        "diskSpaceUsed":"98",
        "totalMapNumber":"100000",
        "checkBlacklisted":"true",
        "whitelisted":""
        }"""
    }
    reData = askFor.post(url, data, jessionId="E095C98CCA90507DCA3DF285E677F766")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.44 添加hadoop集群监控指标配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('添加hadoop集群监控指标配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/addHadoopMPC.md', 'w')
    f.write(data)
    f.close()
    print(data)

#修改hadoop集群监控指标配置
def modifyHadoopMPC():
    url = 'http://192.168.7.80:8080/manage/mobile/hadoopMPC/save'
    data = {
        "version":"hkv1",
        "hadoopMPC":"""{
        "id":"1",
        "created":"2014-4-6 18:49:08",
        "createdBy":"系统管理员",
        "updated":"",
        "updatedBy":"",
        "taskTrackerNumber":"13",
        "datanodeNumber":"13",
        "diskSpaceUsed":"96",
        "totalMapNumber":"100000",
        "checkBlacklisted":"true",
        "whitelisted":""
        }"""
    }
    reData = askFor.post(url, data, jessionId="E095C98CCA90507DCA3DF285E677F766")
    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==3.45 修改hadoop集群监控指标配置==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('修改hadoop集群监控指标配置')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/modifyHadoopMPC.md', 'w')
    f.write(data)
    f.close()
    print(data)
