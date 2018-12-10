import requests
import uuid

params ={
        'action':'list_course',
        'pagenum':1,
        'pagesize':20
    }

name="课程名称4"
uuid = uuid.uuid1()

reqJSONdata = {
    'action':'add_course_json',
    'data':{
                "name":"%s" % name,
                "desc":'%s' % uuid,
                "display_idx":2
            }
}

# print(type(reqJSONdata))
r5 = requests.post("http://localhost:8088/apijson/mgr/sq_mgr/",
                   params=params,
                   json=reqJSONdata)

print(r5.json())


# 设置时间显示
# import datetime
# timeShow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(timeShow)
