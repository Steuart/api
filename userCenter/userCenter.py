import askFor
import API
import hashlib
import time

#md5加密函数
def md5(str):
    m = hashlib.md5()
    m.update(str.encode(encoding="utf-8"))
    return m.hexdigest()


#同步用户信息
def syncUserInfo():
    url = 'http://192.168.7.80/user/synUser'
    password="0d5379fbfde050a2e2186fb2b1ed360f"
    username="lifeng"
    datetime = str(int(time.time()*1000))
    token = md5(password+md5(username+datetime))
    data = {
        "userName":username,
        "password":password,
        "appid":1,
        "token":token,
        "datetime":datetime
    }

    reData = askFor.post(url, data, jessionId="")

    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==1.1 同步用户信息==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe("同步子系统用户信息到用户中心")
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('E:/api/userCenter/user.md', 'w')
    f.write(data)
    f.close()
    print(data)

#调度系统登录
def schedulerLogin():
    url = 'http://192.168.7.80/user/login'

    data = {
        "username": "lifeng",
        "password": "lifeng123",
    }

    reData = askFor.post(url, data, jessionId="")

    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==1.1 同步用户信息==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe("同步子系统用户信息到用户中心")
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('E:/api/userCenter/scheduler.md', 'w')
    f.write(data)
    f.close()
    print(data)

#统一监控系统登录
def monitorLogin():
    url = 'http://192.168.7.80/user/login'

    data = {
        "username": "admin",
        "password": "admin",
    }

    reData = askFor.post(url, data, jessionId="")

    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==1.2 登录==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe("登录")
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('E:/api/userCenter/monitor.md', 'w')
    f.write(data)
    f.close()
    print(data)

#爬虫系统登录
def scrawlerLogin():
    url = 'http://192.168.7.80/user/login'

    data = {
        "username": "admin",
        "password": "123456",
    }

    reData = askFor.post(url, data, jessionId="")

    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==1.2 登录==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe("登录")
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('E:/api/userCenter/spider.md', 'w')
    f.write(data)
    f.close()
    print(data)

#切换时登录子系统
def loginSubSys():
    url = 'http://192.168.7.80/user/loginSubSystem'

    data = {
        "appId": 3,
    }

    reData = askFor.post(url, data, jessionId="YWRtaW4xNDgwNDk3Njc4NzAxYjh3ZEg")

    print(reData)
    Page = API.Page
    page = Page()
    page.setH("==1.3 切换时登录子系统==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe("切换时登录子系统")
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('E:/api/userCenter/loginSubSys.md', 'w')
    f.write(data)
    f.close()
    print(data)

loginSubSys()

