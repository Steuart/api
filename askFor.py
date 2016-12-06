from urllib import request
import urllib
import json
import time
#发送http post请求
def post(url,data,jessionId,type="form"):
    headers = {
        "Accept": "text/json,application/json",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "JSESSIONID="+jessionId,
        ##"Cookie": "token=" + jessionId,
        "Request Method": "POST",
        "x-requested-with":"XMLHttpRequest"
    }

    if(type=="json"):
        headers["Content-Type"]="application/json; charset=UTF-8"
        data = json.dumps(data)
        data = data.encode("utf-8")
    else:
        data = urllib.parse.urlencode(data).encode("utf-8")
    myReq = request.Request(url, data, headers)
    res = request.urlopen(myReq)
    print(str(res.info())+"--------------------------------")
    reData = res.read().decode("utf-8")
    return reData
