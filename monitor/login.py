import askFor
import API

#登录验证
def loginValid():
    url = 'http://192.168.0.2:8080/monitor/manage/mobile/login/validate'
    data = {
        "version":"hkv1",
        "username":"admin",
        "password":"admin"
    }

    reData = askFor.post(url, data,jessionId="")

    Page = API.Page
    page = Page()
    page.setH("==1.1 登录验证==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('账号密码登录信息验证')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/loginvalid.md', 'w')
    f.write(data)
    f.close()
    print(data)

#登录
def login():
    url = 'http://192.168.7.80:8080/monitor/manage_security_login'
    data = {
        "version":"hkv1",
        "j_username":"admin",
        "j_password":"admin"
    }

    reData = askFor.post(url, data,jessionId="")

    Page = API.Page
    page = Page()
    page.setH("==1.1 用户登录==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('用户登录')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/login.md', 'w')
    f.write(data)
    f.close()
    print(data)
login()


#退出
def logout():
    url = 'http://192.168.0.2:8080/monitor/manage_security_logout'
    data = {
        "version":"hkv1"
    }

    reData = askFor.post(url, data,jessionId="DD375EAEFE9129078773B12756DFEACE")

    Page = API.Page
    page = Page()
    page.setH("==1.1 用户退出==", 3)
    page.setMethod('post')
    page.setUrl(url)
    page.setScribe('用户退出')
    page.setReqParams(data)
    page.setReqEx(data)
    page.setResEx(reData)
    page.setResParams(reData)
    data = page.getPage()
    f = open('e:/api/logout.md', 'w')
    f.write(data)
    f.close()
    print(data)
