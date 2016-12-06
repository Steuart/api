import askFor
import API

#删除程序告警状态
def serverList():
    url = 'http://192.168.7.80:8080/manage/mobile/server/list'
    data = {
        "version":"hkv1",
        "condition":{"active-eq":"true"}
    }

    reData = askFor.post(url, data, jessionId="9EC8B5E9A293BFB3FB06DB8C989B98EA")

    Page = API.Page
    page = Page()
    page.setH("==6.1 服务器列表信息==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('服务器列表信息')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/serverList.md', 'w')
    f.write(data)
    f.close()
    print(data)

#用户信息列表
def serverList():
    url = 'http://192.168.7.80:8080/manage/mobile/user/list'
    data = {
        "version":"hkv1",
        "condition":{"active-eq":"true"}
    }

    reData = askFor.post(url, data, jessionId="9EC8B5E9A293BFB3FB06DB8C989B98EA")

    Page = API.Page
    page = Page()
    page.setH("==6.2 用户列表信息==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('用户列表信息')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/userList.md', 'w')
    f.write(data)
    f.close()
    print(data)
#服务器登陆账号
def serverList():
    url = 'http://192.168.7.80:8080/manage/mobile/serverUser/list'
    data = {
        "version":"hkv1",
        "condition":{"active-eq":"true"}
    }

    reData = askFor.post(url, data, jessionId="9EC8B5E9A293BFB3FB06DB8C989B98EA")

    Page = API.Page
    page = Page()
    page.setH("==6.3 服务器登陆用户==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('服务器登陆用户')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/serverUserList.md', 'w')
    f.write(data)
    f.close()
    print(data)

#数据源列表
def datasourceList():
    url = 'http://192.168.7.80:8080/manage/mobile/dataSource/list'
    data = {
        "version":"hkv1",
        "condition":""
    }

    reData = askFor.post(url, data, jessionId="9EC8B5E9A293BFB3FB06DB8C989B98EA")

    Page = API.Page
    page = Page()
    page.setH("==7.1 数据源列表==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('数据源列表')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/datasourceList.md', 'w')
    f.write(data)
    f.close()
    print(data)

#告警策略
def alertStrategyList():
    url = 'http://192.168.0.2:8080/monitor/manage/mobile/alertStrategy/list'
    data = {
        "version":"hkv1",
        "condition":""
    }

    reData = askFor.post(url, data, jessionId="9EC8B5E9A293BFB3FB06DB8C989B98EA")

    Page = API.Page
    page = Page()
    page.setH("==7.2 告警策略列表==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('告警策略列表')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/alertStrategyList.md', 'w')
    f.write(data)
    f.close()
    print(data)

#磁盘空间策略列表
def diskSpaceStrategyList():
    url = 'http://192.168.0.2:8080/monitor/manage/mobile/diskSpaceStrategy/list'
    data = {
        "version":"hkv1",
        "condition":""
    }

    reData = askFor.post(url, data, jessionId="9EC8B5E9A293BFB3FB06DB8C989B98EA")

    Page = API.Page
    page = Page()
    page.setH("==8.3 磁盘空间策略列表==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('磁盘空间策略列表')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/diskSpaceStrategyList.md', 'w')
    f.write(data)
    f.close()
    print(data)

diskSpaceStrategyList()