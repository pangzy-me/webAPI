print('------http协议------单个request请求------')
'''
----------------------------------------------
HTTP请求：四要素【method、URL、header、body】
> method    请求方法
> URL
    URL参数 query string
    encodeURLcomponent
> headers   请求头
> 消息体body(传输数据的一种格式而已)
    application/    x-www-form-ulrencoded
    application/    json
    application/    xml
    multipart/      form-data
    其他
----------------------------------------------
1.postman   设置- general - SSL... 选项关闭，即可。访问https时不加协议。
2.Body      postman消息体，格式。

'''
import pprint
import requests
# r1 = requests.get("http://httpbin.org/get")
# r2 = requests.post("http://httpbin.org/post")

# 设置请求URL中的参数为字典，可以方便使用特殊字符。参数放在URL中的。
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
# r3 = requests.get("http://localhost:8088/api/mgr/sq_mgr/",
#                   params=parms,
#                   headers=reqHeaders)
# responseJSONobj = r3.json()
# pprint.pprint(responseJSONobj)
# 1.设置body
# data 记录默认消息体中数据格式为content-type:application/x-www-form-urlencoded
# data 为字典，如果换行需使用换行符'''xxxxxxxxxx'''
# reqData = {
#     'action':'add_course',
#     'data':'''
#         {
#             "name":"课程名称",
#             "desc":"课程描述",
#             "display_idx":2
#         }
#     '''
# }
# r4 = requests.post("http://localhost:8088/api/mgr/sq_mgr/",
#                    headers=reqHeaders,
#                    data=reqData)

# 2.设置body
# json格式的方法构建。消息体中数据格式为json。content-type:application/json
reqJSONdata = {
    'action':'add_course_json',
    'data':{
                "name":"课程名称jsond5",
                "desc":'课程描述jsond5',
                "display_idx":2
            }
}
# 注意此时双引号，单引号都行，Python中会自动转为双引号字符串。
r5 = requests.post("http://localhost:8088/apijson/mgr/sq_mgr/",
                   headers=reqHeaders,
                   params=parms,
                   json=reqJSONdata)
# 接收请求返回的消息体数据
print(r5.text)
# 用断言验证返回结果数据
# assert '"retcode": 0' in r5.text

