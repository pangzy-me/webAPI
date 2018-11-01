import requests

print('------request请求组合成函数------')

def fun_get():
    parms ={
        'action':'list_course',
        'pagenum':1,
        'pagesize':20
    }
    # 设置请求头header。放在消息头中的。
    reqHeaders = {
        'username':'zhangsan',
        'password':'111111'
    }
    r3 = requests.get("http://localhost:8088/api/mgr/sq_mgr/",
                      params=parms,
                      headers=reqHeaders)
    return r3

def fun_post(name,desc,idx):
    reqData = {
        'action':'add_course',
        'data':'''
            {
                "name":"%s",
                "desc":"%s",
                "display_idx":"%s"
            } ''' % (name,desc,idx)
    }
    r4 = requests.post("http://localhost:8088/api/mgr/sq_mgr/",
                       data=reqData)
    # retObject = r4.json()
    # pprint.pprint(retObject)
    return r4
# get = fun_get()
# pprint.pprint(get.json())
# time.sleep(2)
retObj = fun_post("检查课程","检查课程","5").json() ## 操作返回的一个数据对象，单引号，双引号都可以。
assert retObj["retcode"] == 2
# time.sleep(2)
# get = fun_get()
# pprint.pprint(get.json())

# 设置时间显示
# import datetime
# timeShow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(timeShow)