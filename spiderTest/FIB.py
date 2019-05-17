from datetime import datetime as dt
import requests as rq
import json
# 预约函数
def book_FIB(st,ed):
    # st=btime[4:20]
    # ed=btime[4:15]+btime[21:26]
    URL='http://samp.cas.cn/sams/loginForUI3Action.do?method=logon'
    headers={'Host': 'samp.cas.cn',
             'Referer': 'http://samp.cas.cn/admin.jsp',
             'Use-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

    postData={'usercode': 'ipwlsjiyiru',
              'passwd': 'z1a2q3#*'}
    iop_se=rq.Session()
    responseRes=iop_se.post(URL,data=postData,headers=headers)
    #print(responseRes.text)

    URL='http://samp.cas.cn/sams/ordApplyAction.do?method=doSubmitQuickApply'
    headers={'Host': 'samp.cas.cn',
             'Referer': 'http://samp.cas.cn/sams/ordApplyAction.do?method=doApply&ordModelType=2&apparIds=13713',
             'Use-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

    postData={'apparatusId': '13713',
              'apparatusName': '聚集离子束/电子束双束Helios 600I 系统',
              'jsonArray':json.dumps([{"title":st+"&"+ed,"start":st, "end":ed}])
              }
    responseRes=iop_se.post(URL,data=postData,headers=headers)
    return(responseRes.text)

if __name__ == '__main__':

    # open the file and read
    # f=open('C:\\Users\\User\\Documents\\python_lml\\FIB.txt')
    f = open('./FIB.txt')
    lines=f.readlines()
    f.close()
    #creat new file
    # f=open('C:\\Users\\User\\Documents\\python_lml\\FIB.txt','w')
    f = open('./FIB.txt','r+')
    for line in lines:
        bt=dt.strptime(line[4:20],'%Y-%m-%d %H:%M')
        #    det=(bt-dt.strpt ime('2019-01-03 00:00','%Y-%m-%d %H:%M')).days
        det=(bt-dt.now()).days
        if det==13:
            #        print(line)
            #        print(det)
            result=book_FIB(line)
            #        line=line.replace('\n',' '+'book\n')
            line=line.replace('\n',' '+result[11:18]+'\n')
        #        print(line)
        elif det<0:
            break
        f.write(line)
        print(dt.now(),line)
    f.close()
