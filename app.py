import json as chenhao
from base64 import b64decode
from base64 import b64encode

import ddddocr
from flask import Flask, render_template, json, request
from gevent import pywsgi

import config

app = Flask(__name__)
app.config.from_object(config)

ocr = ddddocr.DdddOcr(old=True, show_ad=False)


# 图片  转    base64
def picture2base(path):
    with open(path, 'rb') as img:
        # 使用base64进行编码
        b64encodes = b64encode(img.read())
        s = b64encodes.decode()
        base64 = 'data:image/jpeg;base64,%s' % s
        # 返回base64编码字符串
        return base64


# base64  转    成图片
def base2picture(var):
    strs = var.split(',')[1]
    imgdata = b64decode(strs)
    file = open('test.jpg', 'wb')
    file.write(imgdata)
    file.close()


# base64通过json上传
@app.route('/imgBase64JSON', methods=['POST'])
def sysconfig_save_jsonstr():
    try:
        data = request.get_data()
        data = json.loads(data)

        # # 校验token
        # request_token = data['token']
        # if not request_token:
        #     return chenhao.dumps({
        #         "status": 200,
        #         "message": "token 没有"
        #     }), 200, {"Content-Type": "application/json"}

        var = data['img']

        base2picture(var)

        with open("test.jpg", 'rb') as f:
            image = f.read()

        # print(b64decode(image))
        res = ocr.classification(image)

        print(res)

        result = {
            "status": 200,
            "message": res
        }

        # print(res)

        return chenhao.dumps(result), 200, {"Content-Type": "application/json"}

    except Exception as e:
        return e


# ping接口
@app.route('/ping', methods=['GET'])
def ping():
    result = {
        "status": 200,
        "message": "pong"
    }
    return chenhao.dumps(result), 200, {"Content-Type": "application/json"}


# form表单上传文件
@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['img']
    file.save('test.jpg')

    with open("test.jpg", 'rb') as f:
        image = f.read()

    res = ocr.classification(image)
    print(res)
    return render_template('show.html', str=res)


# ========== page ==========
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 8787), app)
    print("server start")
    server.serve_forever()
