import os
import minidb
# minidb.loadJson( jsonFile = 'datas.json')
#minidb.saveJson(parsedDict,jsonFile)
# minidb.saveVarjson(parsedDict,jsonFile,varName='datas')
import fluiddb
#fluidset(no)
#fluid[no]['유저태그']=[]
#addn(user,no,key)
# addtagu(user,no,text)
# addtag(user,no,text)
# addcomm(user,no,text,time)
from jsonio import *

from flask import send_from_directory, send_file
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)






#--------------------------------------------------------
#i love it! it exports only if is.
#it became datas in html. used for makebox.
def getHeaddict(datas):
    headKeys = ['제목','날짜','리사이즈','캐릭터태그' ]#'조','추','좋'
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
def getfluiddict(datas):
    headKeys = ['제목','날짜','리사이즈','캐릭터태그' ]#'조','추','좋'
    headDict = {}

    for k in fluiddb.fluid:
        tmplist=[]
        headDict[k]={}
        for tk in fluiddb.fluid[k]['캐릭터태그']:
            tmplist.append( fluiddb.fluid[k]['캐릭터태그'][tk]['text'] )
            headDict[k]['캐릭터태그'] = tmplist

    # for key in datas.keys():
    #     tempDict = {}
    #     for k in datas[key].keys():
    #         if k in headKeys:
    #             tempDict[k] = datas[key][k]
    #             #print(d[k])
    #     headDict[key] = tempDict
    return headDict





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


logue = []
datas = {}
@app.route('/getjson')
def getJson():
    global datas

    jsonName = 'datas.json'
    datas = minidb.loadJson( jsonName )
    print('datas len : ',len(datas))
    fluiddb.fluid = loadJson( 'fluid_backup0.txt' )
    print('fluid len : ',len(fluiddb.fluid))

    #jsonName = 'datas.json'
    #datas = minidb.loadJson( jsonName )
    return 'datas'+str(len(datas))+'fluid'+str(len(fluiddb.fluid))

@app.route('/jarscan')
def jarScan():
    global datas
    no = backupDatas(datas)
    datas = minidb.jarScan(datas)
    return "backup no:"+str(no)+'jarscan after:'+str(len(datas))

@app.route('/headexport')
def headExport():
    global datas
    headdictPath = './static/headdict.json'
    headDict = getHeaddict(datas)
    print('headDict: ',len(headDict))
    minidb.txt2dict.saveVarjson(headDict,headdictPath,'datas')

    fluiddictPath = './static/fluiddict.json'
    #fluidDict = fluiddb.fluid
    fluidDict = getfluiddict(fluiddb.fluid)
    print('fluidDict: ',len(fluidDict))
    minidb.txt2dict.saveVarjson(fluidDict,fluiddictPath,'fluid')
    return 'fluidexport'

@app.route('/backupdatas')
def backup():
    global datas
    print(datas)
    nostr = backupDatas(datas)
    return str(len(datas))+'datas backup no: '+nostr
datas = {}
def backupDatas(datas=datas):
    print(datas)
    flist = os.listdir()
    no=0
    while 'b{}_datas.json'.format(no) in flist:
        no+=1
    print('backup no:',no)
    #datasdictPath = './b_datas.json'
    datasdictPath = './b{}_datas.json'.format(no)
    print('datas len: ',len(datas))
    minidb.txt2dict.saveJson(datas,datasdictPath)
    return str(no)

#이거보단명령어.ㅇㅋ. fluiddb.fluid[no]['캐릭터태그']

tdict={}
@app.route('/fetchtag')
def fetchtag():
    global datas
    global tdict
    #print(request.query_string)
    no = request.args.get('no')
    taglist = request.args.get('taglist')
    taglist = taglist.split(',')
    #tdict[no]=taglist
    taglist = list(set(taglist))

    if taglist[0]=='뮤즈':
        taglist=['호노카','코토리','우미','마키','린','하나요','에리','니코','노조미']



    no=str(no)
    user='핫산테크'
    key='캐릭터태그'
    if taglist[0]=='':
        fluiddb.retext(user,no,key,)

    if fluiddb.fluidset(no) == True:#made this time.
        for text in taglist:
            if fluiddb.addtext(user,no,key,text) != True:
                print('NEVER SEE THIS error but exception it exit.bad!')
            else:
                print('add first ok')
    else:#alreadywas. rewrite
        fluiddb.retext(user,no,key,)
        for text in taglist:
            #fluiddb.subtext(user,no,key,text)
            fluiddb.addtext(user,no,key,text)
            #print('subtext', fluiddb.subtext(user,no,key,text) )
            #print('addagain', fluiddb.addtext(user,no,key,text) )
    #fluiddb.addn(user,no,'조')
    print(no,taglist)
    return 'ok'

@app.route('/backup')
def backupfluid():
    fluiddb.backupfluid()
    fluiddb.backuplogue()
    ma = str(len(fluiddb.fluid))
    return ma


@app.route('/tagsave')
def tagdictsave():
    global tdict
    #saveJson(tdict,'tagdict.json')
    #ma='oksave'+str(len(tdict))
    fluiddb.backupfluid()
    ma = str(len(fluiddb.fluid))
    return ma

#toolong @app.route('/fetch/bodytext/<path:no>')
@app.route('/fetch')
def fetchParse():
    global datas
    no = request.args.get('no')
    key = request.args.get('key')
    #request.query_string
    print(no,key)
    valueText = datas[no][key]
    print(valueText)
    #return( valueText )
    #data = {'server_name' : '0.0.0.0', 'server_port' : '8080'}# it! works!
    data = { 'bodytext':valueText }
    return jsonify(data)

@app.route('/heavyfetch')
def heavyfetchParse():
    global datas
    global fluid
    #no = request.args.get('no')
    key = request.args.get('key')
    #request.query_string
    tmplist=[]
    tmplist2=[]
    tmpdict={}
    for n in fluid:
        tmpdict[n] = fluid[n][key]

    valueText = datas[no][key]
    print(no,key)
    print(valueText)
    #return( valueText )
    #data = {'server_name' : '0.0.0.0', 'server_port' : '8080'}# it! works!
    data = { 'bodytext':valueText }
    return jsonify(data)

@app.route('/bodyload')
def bodyload():
    global datas
    global fluid
    key = request.args.get('key')
    tmpdict[n] = fluid[n][key]
    data = { 'bodytext':valueText }
    return jsonify(data)





if __name__ == "__main__":
    
    try:
        jsonName = 'datas.json'
        datas = minidb.loadJson( jsonName )
        print('datas len : ',len(datas))
        fluiddb.fluid = loadJson( 'fluid_backup0.txt' )
        print('fluid len : ',len(fluiddb.fluid))
    except:
        print('no dict')
    app.run(debug = False, host='0.0.0.0' , port = '12800')
