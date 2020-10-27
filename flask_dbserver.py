import os
import minidb

from flask import send_from_directory, send_file
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)






#--------------------------------------------------------
#i love it! it exports only if is.

def getHeaddict(datas):
    headKeys = ['제목','날짜','리사이즈','태그', '유저태그', '조회수','댓글수','추천수']
    headDict = {}
    for d in datas.values():
        tempDict = {}
        for k in d.keys():
            if k in headKeys:
                tempDict[k] = d[k]
                #print(d[k])
        headDict[d['번호']] = tempDict
    return headDict
#--------------------------------------------------------






@app.route('/')
def hellow():
   return 'hello'


#업로드 HTML 렌더링
@app.route('/upload')
def render_file():
   return render_template('upload.html')

#업로드 HTML 렌더링
@app.route('/view')
def viewmain():
   return render_template('rocketbox.html')

@app.route('/dview')
def dviewmain():
   return render_template('highspeedtag.html')

@app.route('/file/<path:filenameinput>', methods=['GET', 'POST'])
def download(filenameinput):
    # 디렉터리에선 폴더명이다. upload 로 s안붙이니 안나왔음;
    #파일네임을 입력을 받은걸, 어떻게든 넘기는구조같다.
    #디렉터리에서 파일을 보내는 함수라는것은 알겠어..
    return send_from_directory(directory='uploads', filename=filenameinput)

@app.route('/static/<path:filenameinput>', methods=['GET', 'POST'])
def staticFile(filenameinput):
    # 디렉터리에선 폴더명이다. upload 로 s안붙이니 안나왔음;
    #파일네임을 입력을 받은걸, 어떻게든 넘기는구조같다.
    #디렉터리에서 파일을 보내는 함수라는것은 알겠어..
    print('filenameinput',filenameinput)
    #return send_file( filename=filenameinput )
    return send_file( filename_or_fp = filenameinput )
    #http://localhost:12800/static/mah.txt로 접속시,staic폴더안에연결됨.ㅇㅋ


@app.route('/server_info')
def hello_json():
    data = {'server_name' : '0.0.0.0', 'server_port' : '8080'}
    return jsonify(data)









datas = {}
@app.route('/getjson')
def getJson():
    global datas
    jsonName = 'datas.json'
    datas = minidb.loadJson( jsonName )
    return( str(len(datas)))

@app.route('/jarscan')
def jarScan():
    global datas
    datas = minidb.jarScan(datas)
    return( str(len(datas)))

@app.route('/headexport')
def headExport():
    global datas
    headdictPath = './static/headdict.json'
    headDict = getHeaddict(datas)
    print('headDict: ',len(headDict))
    minidb.txt2dict.saveVarjson(headDict,headdictPath,'datas')
    return 'headgone'

@app.route('/backupdatas')
def backupDatas():
    global datas
    flist = os.listdir()
    no=0
    while 'b{}_datas.json'.format(no) in flist:
        no+=1
    print(no)
    #datasdictPath = './b_datas.json'
    datasdictPath = './b{}_datas.json'.format(no)
    print('datas: ',len(datas))
    minidb.txt2dict.saveJson(datas,datasdictPath)
    return 'datas saved'



#toolong @app.route('/fetch/bodytext/<path:no>')
@app.route('/fetch')
def fetchParse():
    global datas
    no = request.args.get('no')
    key = request.args.get('key')
    #request.query_string
    valueText = datas[no][key]
    print(no,key)
    print(valueText)
    #return( valueText )
    #data = {'server_name' : '0.0.0.0', 'server_port' : '8080'}# it! works!
    data = { 'bodytext':valueText }
    return jsonify(data)


if __name__ == "__main__":
    jsonName = 'datas.json'
    try:
        datas = minidb.loadJson( jsonName )
        print('datas len : ',len(datas))
    except:
        print('no dict')
    app.run(debug = False, host='0.0.0.0' , port = '12800')
