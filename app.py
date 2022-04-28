import json

from flask_cors import CORS

from compare import compareTwo

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
app.debug = True
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def hello_world():
    return render_template('compare.html')


@app.route('/compare', methods=['post'])
def compare():
    if not request.data:  # 检测是否有数据
        return ('fail')
    all = request.data.decode('utf-8')
    # 获取到POST过来的数据，因为我这里传过来的数据需要转换一下编码。根据晶具体情况而定
    all_json = json.loads(all)
    # 把区获取到的数据转为JSON格式。

    mytext = all_json['mytext']
    para = all_json['para']
    try:
        percent = all_json['persent']
    except KeyError as e:
        print(e)
        res = compareTwo(mytext, para, None)
        return jsonify(res)
    else:
        res = compareTwo(mytext, para, int(percent))
        return jsonify(res)
    # 返回JSON数据。


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)
    # 这里指定了地址和端口号。
