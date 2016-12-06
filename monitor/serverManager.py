#服务器管理

import askFor
import API

#获取服务器管理分页列表
def serverManagePage():
    url = 'http://192.168.7.80:8080/manage/mobile/server/paging'
    data = {
        "version":"hkv1",
        "start":0,
        "limit":15,
        "condition":"""{"name":"","ip":"","manager":""}"""
    }

    reData = askFor.post(url, data,jessionId="FD1807345BCB075B11B95C987B13483C")

    Page = API.Page
    page = Page()
    page.setH("==5.1 获取服务器管理分页列表==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('获取服务器管理分页列表')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/serverManagePage.md', 'w')
    f.write(data)
    f.close()
    print(data)

#添加服务器管理
def addServerManagePage():
    url = 'http://192.168.7.80:8080/manage/mobile/server/save'
    data = {
        "version":"hkv1",
        "server":"""{
        "id":"",
        "created":"2016-6-23 13:05:46",
        "createdBy":"系统管理员",
        "updated":"2016-6-23 13:05:25",
        "updatedBy":"系统管理员",
        "name":"dc-hadoop110",
        "ip":"192.168.0.110",
        "manager":"1",
        "description":"这是一个测试"
        }"""
    }

    reData = askFor.post(url, data,jessionId="FD1807345BCB075B11B95C987B13483C")

    Page = API.Page
    page = Page()
    page.setH("==5.2 添加服务器管理==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('添加服务器管理')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/addServerManage.md', 'w')
    f.write(data)
    f.close()
    print(data)

#修改服务器管理
def modifyServerManagePage():
    url = 'http://192.168.7.80:8080/manage/mobile/server/save'
    data = {
        "version":"hkv1",
        "server":"""{
        "id":"6",
        "created":"2016-6-23 13:05:46",
        "createdBy":"系统管理员",
        "updated":"2016-6-23 13:05:25",
        "updatedBy":"系统管理员",
        "name":"dc-hadoop110",
        "ip":"192.168.0.110",
        "manager":"1",
        "description":"这是一个测试修改"
        }"""
    }

    reData = askFor.post(url, data,jessionId="FD1807345BCB075B11B95C987B13483C")

    Page = API.Page
    page = Page()
    page.setH("==5.3 修改服务器管理==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('修改服务器管理')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/modifyServerManage.md', 'w')
    f.write(data)
    f.close()
    print(data)

#禁用服务器管理
def logicRemoveServerManagePage():
    url = 'http://192.168.7.80:8080/manage/mobile/server/logicRemove'
    data = {
        "version":"hkv1",
        "id":6
    }

    reData = askFor.post(url, data,jessionId="47A578BAA1F73B5D6F0833EEF16CB5C9")

    Page = API.Page
    page = Page()
    page.setH("==5.4 禁用服务器管理==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('禁用服务器管理')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/logicRemoveServerManage.md', 'w')
    f.write(data)
    f.close()
    print(data)

#恢复服务器管理
def recoveryServerManagePage():
    url = 'http://192.168.7.80:8080/manage/mobile/server/recovery'
    data = {
        "version":"hkv1",
        "id":6
    }

    reData = askFor.post(url, data,jessionId="47A578BAA1F73B5D6F0833EEF16CB5C9")

    Page = API.Page
    page = Page()
    page.setH("==5.5 恢复服务器管理==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('恢复服务器管理')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/recoveryServerManage.md', 'w')
    f.write(data)
    f.close()
    print(data)

#服务器账号分页列表
def serverUserPage():
    url = 'http://192.168.7.80:8080/manage/mobile/serverUser/paging'
    data = {
        "version":"hkv1",
        "start":0,
        "limit":15,
        "condition":"""{"username":""}"""
    }

    reData = askFor.post(url, data,jessionId="0ACD9AF0BA378527E157C65C1D51B8DA")

    Page = API.Page
    page = Page()
    page.setH("==5.6 获取服务器账号分页列表==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('获取服务器账号分页列表')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/serverUserPage.md', 'w')
    f.write(data)
    f.close()
    print(data)

#添加服务器账号
def addServerUser():
    url = 'http://192.168.7.80:8080/manage/mobile/serverUser/save'
    data = {
        "version":"hkv1",
        "serverUser":"""{
        "id":"",
        "created":"2016-6-23 13:07:17",
        "createdBy":"系统管理员",
        "updated":"2016-7-10 11:02:59",
        "updatedBy":"系统管理员",
        "username":"root",
        "password":"123456a",
        "name":"root",
        "description":"这是一个测试"
        }"""
    }

    reData = askFor.post(url, data,jessionId="0ACD9AF0BA378527E157C65C1D51B8DA")

    Page = API.Page
    page = Page()
    page.setH("==5.7 添加服务器账号==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('添加服务器账号')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/addServerUser.md', 'w')
    f.write(data)
    f.close()
    print(data)

#修改服务器账号
def modifyServerUser():
    url = 'http://192.168.7.80:8080/manage/mobile/serverUser/save'
    data = {
        "version":"hkv1",
        "serverUser":"""{
        "id":"2",
        "created":"2016-6-23 13:07:17",
        "createdBy":"系统管理员",
        "updated":"2016-7-10 11:02:59",
        "updatedBy":"系统管理员",
        "username":"test",
        "password":"123456a",
        "name":"test",
        "description":"这是一个测试"
        }"""
    }

    reData = askFor.post(url, data,jessionId="0ACD9AF0BA378527E157C65C1D51B8DA")

    Page = API.Page
    page = Page()
    page.setH("==5.8 修改该服务器账号==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('修改服务器账号')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/modifyServerUser.md', 'w')
    f.write(data)
    f.close()
    print(data)


#禁用服务器账号
def logicRemoveServerUser():
    url = 'http://192.168.7.80:8080/manage/mobile/serverUser/logicRemove'
    data = {
        "version":"hkv1",
        "id":"2"
    }

    reData = askFor.post(url, data,jessionId="D494ED46A6979247C131874CA0637F67")

    Page = API.Page
    page = Page()
    page.setH("==5.9 禁用服务器账号==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('禁用服务器账号')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/logicRemoveServerUser.md', 'w')
    f.write(data)
    f.close()
    print(data)

#恢复服务器账号
def recoveryServerUser():
    url = 'http://192.168.7.80:8080/manage/mobile/serverUser/recovery'
    data = {
        "version":"hkv1",
        "id":"2"
    }

    reData = askFor.post(url, data,jessionId="D494ED46A6979247C131874CA0637F67")

    Page = API.Page
    page = Page()
    page.setH("==5.10 恢复服务器账号==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('恢复服务器账号')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/recoveryServerUser.md', 'w')
    f.write(data)
    f.close()
    print(data)

#修改服务器账号密码
def passwordServerUser():
    url = 'http://192.168.7.80:8080/manage/mobile/serverUser/password'
    data = {
        "version":"hkv1",
        "serverUserId":2,
        "password":123456
    }

    reData = askFor.post(url, data,jessionId="07DA34EA459B8DE5C4CC041FE401BCEE")

    Page = API.Page
    page = Page()
    page.setH("==5.11 修改服务器账号密码==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('修改服务器账号密码')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/passwordServerUser.md', 'w')
    f.write(data)
    f.close()
    print(data)
passwordServerUser()