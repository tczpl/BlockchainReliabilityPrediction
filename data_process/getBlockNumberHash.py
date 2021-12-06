import os
import json
import pandas as pd
import requests

blocknumber = pd.Series()
f = open('BlockNumberHash.csv', 'w')

def eachFile(srcDataPath):
    pathDir =  os.listdir(srcDataPath)
    for ip in pathDir:
        readFile(ip)

def to10(x):
    if (pd.isnull(x)):
        return x
    else:
        return int(x,16)

def readFile(ip):
    global blocknumber
    jsons=[]
    filename = srcDataPath+ip+"/output.txt"
    fopen = open(filename, 'r') # r 代表read
    for eachLine in fopen:
        jsonstr = '{'+eachLine[:-2]+'}'
        jsons.append(json.loads(jsonstr))
    fopen.close()
    df = pd.DataFrame(jsons)
    uni = pd.Series(df['number'].unique())
    blocknumber = blocknumber.append(uni)
    print(blocknumber.unique().shape)

def reqandwrite(block):
    global f
    if(pd.isnull(block)):
        return
    print("block", block)
    jsonreq = '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["'+block+'",false],"id":666}'
    response = requests.post('https://mainnet.infura.io',data=jsonreq, headers={'Content-type':'application/json'})
    getjson = json.loads(response.text)
    if (getjson['result']!=None):
        towrite = block+","+getjson['result']['hash']+"\n"
        f.write(towrite)



if __name__ == '__main__':
    srcDataPath = "../100x200src/"
    eachFile(srcDataPath)
    pd.Series(blocknumber.unique()).to_csv("blocknumber.txt")
    cnt = 0
    for i in blocknumber.unique():
        reqandwrite(i)
        cnt+=1
        print(cnt)
    f.close()