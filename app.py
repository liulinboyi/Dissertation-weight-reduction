import json
from compare import compareTwo

from flask import Flask, request, jsonify

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return 'Hello from Flask Github!'


@app.route('/compare', methods=['post'])
def compare():
    if not request.data:  # 检测是否有数据
        return ('fail')
    all = request.data.decode('utf-8')
    # 获取到POST过来的数据，因为我这里传过来的数据需要转换一下编码。根据晶具体情况而定
    all_json = json.loads(all)
    # compare(all_json)
    # 把区获取到的数据转为JSON格式。

    # json_data = request.get_json()
    mytext = all_json['mytext']
    para = all_json['para']
    res = compareTwo(mytext, para)
    return jsonify(res)
    # 返回JSON数据。


#
# # if __name__ == '__main__':
# #     app.run(host='192.168.1.154',port=1234)
# #     #这里指定了地址和端口号。

#
# from flask import Flask, request
# import requests
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello from Flask Github!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)
    # 这里指定了地址和端口号。
