# -*- coding: utf-8 -*
import flask
import time
import random
import string
import json
import os
#import pdf
import sys
os.chdir(sys.path[0])
# 首先app = Flask(__name__)这部分是一个初始化的过程;__name__代表当前的python文件。把当前的python文件当做一个服务启动
server = flask.Flask(__name__)


@server.route('/apigetpost', methods=['get', 'post'])
def apigetpost():
    global arr
    if flask.request.method == 'GET':
        # name = "get"
        # name = "post"
        # print("post")
        # print(flask.request.headers)
        # print(flask.request.form)
        # arr1 = ["1", "2", "3", "4"]
        # print(arr1)
        # data1 = [u'12th October,2021', u'carlxjs business name ',
        #          u'1009-1547', u'bbb', u'mm', u'sss', u'N', u'Y', u'', u'']
        # print(data1)
        # arr = map(str, data1)
        # pdf.test(arr, './', 'name123')
        args_1 = flask.request.args.get("name")
        args_2 = flask.request.args.get("htmltxt")
        args_3 = flask.request.args.get("args_3")

        # data1 = flask.request.get_json()
        # json_str = json.dumps(data1)
        # data2 = json.loads(json_str)
        # print(data2['text'])

        # arr = data2['text']
        # print("tessfaldfja;")
        # arr.encode("utf-8")
        # pdf.test(arr, './', 'name123')
        # print("tessfaldfja;")
    else:
        name = "post"
        print("post")
        print(flask.request.headers)
        print(flask.request.form)
        data1 = flask.request.get_json()
        json_str = json.dumps(data1)
        data2 = json.loads(json_str)
        arrlist = data2['text']
        arr = map(str, arrlist)
        print (arr)
        # pdf.test(arr, './', 'name123')

    # name = flask.request.form.get('name', '')
#    http://127.0.0.1:8888/apigetpost?name=name&htmltxt=132132werwrw
# http://18.167.106.12:8888/apigetpost?name=name&htmltxt=132132werwrw
    # time.sleep(10)
    # arr = ['12th October,2021', 'carlxjs business name ',
    #        '1009-1547', 'bbb', 'mm', 'sss', 'N', 'Y', '', '']
    args_1 = flask.request.args.get("name")
    args_2 = flask.request.args.get("htmltxt")
    args_3 = flask.request.args.get("args_3")
    namestr = arr[1]
    name = namestr.replace(" ", "_")
    pdfrandom = ''.join(random.sample(
        string.ascii_letters + string.digits, 50))
    path = "./pdf"
    # 本地pdf 存放路
    pathpdf = path+"/" + name + "/" + pdfrandom + "/" + name
    print (pathpdf)
    pathpdf1 = path+"/" + name + "/" + pdfrandom
    print (pathpdf1)
    # s3 pdf 存放路径
    pathawssync = "s3://okijkmnjkiuijygtrfdewsaqwsdef/pdf/"
    print (pathawssync)
    # s3 pdf 判断路径
    pathawsexists = "aws s3 ls " + "okijkmnjkiuijygtrfdewsaqwsdef/pdf/" + \
        name + "/" + pdfrandom + "/agree.pdf"
    # 返回路径
    # 调用生成pdf 方法
    #pdf.pdf(arr, pathpdf1, name)

    # pdf.pdf([1,2,3,4,5,6,7,8,9,1],pathpdf1,"name1")
    # 判断pdf 是否生成
    # TEST
    # os.mknod(pathpdf1+"/test.pdf")
    TEST = True
    TEST = False

    if TEST:

        return flask.jsonify({"path": "https://wristcheckpdf.s3.ap-east-1.amazonaws.com/all/8CBrL6gAou3NsxpYO7RJ/test.pdf", "message": "other"})
    for num in range(1, 10):

        print(num)
        # 判断是否存在文件
        if (os.path.exists(pathpdf)):
            print(pathpdf)
            print("存在")
            # aws 同步
            pwdsync = "aws s3 sync ./pdf " + pathawssync

            try:
                os.popen(pwdsync)
            except Exception as e:
                return flask.jsonify({"code": "404", "message": e})
            # aws  是否上传成功
            exists = os.popen(pathawsexists)
            print(pathawsexists)
            print(exists)
            if (exists):
                print("aws 存在 这个文件")
                break
        else:
            print("不存在")
            if (num > 2):

                if not os.path.exists(pathpdf1):
                    os.makedirs(pathpdf1)
                    os.mknod(pathpdf1+"/agree.pdf")
                    print(num)

            time.sleep(2)
    try:
        response = flask.make_response(
            flask.send_from_directory(path, "test1.pdf", as_attachment=True))
        return response
    except Exception as e:
        # return flask.jsonify({"code": "not find", "message": "{}".format(e)})
        return flask.jsonify({"path": "https://okijkmnjkiuijygtrfdewsaqwsdef.s3.ap-east-1.amazonaws.com/pdf/"+name + "/" + pdfrandom + "/agree.pdf", "message": "other"})

    # res = {
    #     "args_1": args_1,
    #     "args_2": args_2
    # }
    # return json.dumps(res,  ensure_ascii=False)


server.run(port=8888, debug=True, host='0.0.0.0')
