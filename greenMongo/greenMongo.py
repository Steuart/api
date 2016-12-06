#青芒果接口
import askFor
import API

#同步用户信息
def test():
    url = 'http://localhost:8080/webservice/order_test'
    data = {
        'username':'hello',
        'password':'1211111111111111',
        'json':"""{
            'a':1,
            'b':2
        }""",
        'order':""""{
            'productID':"1212121212",
            'productNumber':1000,
            'productName':'hhhh'
        }"""
    }

    reData = askFor.post(url, data, jessionId="F2A58C6BA615A6E3767BB95A808AD30D")

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
    f = open('E:/api/greenMongo/greenMongo.md', 'w')
    f.write(data)
    f.close()
    print(data)
test()