import os
import json
import pandas as pd



peers = ["http://159.69.46.179:8545","http://39.104.74.146:8545","http://47.74.38.125:8545","http://ec2-52-38-253-177.us-west-2.compute.amazonaws.com:8545","http://47.98.105.244:8545","http://47.88.189.195:8545","http://116.62.12.249:8545","http://178.128.204.23:8545","http://35.186.151.167:8545","http://35.205.112.90:8545","http://35.198.134.98:8545","http://35.225.161.145:8545","http://150.109.43.127:8545","http://18.213.180.49:8545","http://47.52.174.15:8545","http://106.3.36.150:8545","http://ec2-52-69-166-207.ap-northeast-1.compute.amazonaws.com:8545","http://122.215.240.181:8545","http://ec2-34-204-100-153.compute-1.amazonaws.com:8545","http://122x215x240x182.ap122.ftth.ucom.ne.jp:8545","http://101.37.12.209:8545","http://47.93.181.217:8545","http://47.74.129.126:8545","http://128.199.160.217:8545","http://47.75.80.52:8545","http://106.120.71.212:8545","http://34.220.66.196:8545","http://ec2-52-91-30-201.compute-1.amazonaws.com:8545","http://118.31.166.41:8545","http://47.99.43.77:8545","http://222.143.26.165:8545","http://121.78.3.151:8545","http://34.236.144.91:8545","http://112.74.180.221:8545","http://159.69.26.191:8545","http://147.75.80.165:8545","http://47.90.2.11:8545","http://54.197.98.99:8545","http://18.219.86.142:8545","http://112.74.161.91:8545","http://95.143.85.101:8545","http://18.194.90.118:8545","http://18.188.194.137:8545","http://118.89.52.82:8545","http://116.62.100.69:8545","http://47.98.209.160:8545","http://54.169.164.110:8545","http://210.181.103.62:8545","http://47.74.178.62:8545","http://13.125.67.132:8545","http://18.219.171.162:8545","http://65.49.235.155:8545","http://54.167.54.36:8545","http://ec2-35-176-224-139.eu-west-2.compute.amazonaws.com:8545","http://176.34.19.187:8545","http://ec2-52-52-64-60.us-west-1.compute.amazonaws.com:8545","http://101.200.32.35:8545","http://52.78.219.154:8545","http://139.199.38.130:8545","http://18.211.119.235:8545","http://188.227.17.176:8545","http://54.249.49.189:8545","http://147.75.111.247:8545","http://178.128.252.30:8545","http://ec2-54-169-3-208.ap-southeast-1.compute.amazonaws.com:8545","http://120.79.156.40:8545","http://47.75.91.163:8545","http://39.106.24.183:8545","http://35.164.225.188:8545","http://34.214.43.223:8545","http://185.22.61.111:8545","http://159.203.171.169:8545","http://static.172.144.216.95.clients.your-server.de:8545","http://47.52.118.122:8545","http://18.191.214.222:8545","http://52.19.63.244:8545","http://159.65.3.252:8545","http://sisko.box.kairo.at:8545","http://159.203.77.71:8545","http://159.89.40.251:8545","http://ec2-18-182-15-13.ap-northeast-1.compute.amazonaws.com:8545","http://47.95.255.48:8545","http://23.111.173.210:8545","http://47.96.72.125:8545","http://ec2-34-228-41-220.compute-1.amazonaws.com:8545","http://52.14.8.53:8545","http://47.75.109.241:8545","http://178.128.76.68:8545","http://docker2.realidadfutura.net:8545","http://147.75.100.193:8545","http://159.138.22.142:8545","http://47.89.179.248:8545","http://52.187.147.199:8545","http://23-111-129-50.static.hvvc.us:8545","http://51.15.114.32:8545","http://54.186.106.158:8545","http://54.164.181.159:8545","http://ec2-34-220-126-98.us-west-2.compute.amazonaws.com:8545","http://47.98.252.101:8545","http://118.24.16.191:8545","http://54.91.124.198:8545","http://18.211.234.172:8545","http://46.53.144.128:8545","http://118.226.204.35.bc.googleusercontent.com:8545","http://18.236.124.155:8545","http://34.217.13.70:8545","http://120.131.11.164:8545","http://47.91.108.90:8545","http://167.99.147.27:8545","http://47.92.73.174:8545","http://188.166.121.96:8545","http://ec2-54-222-133-149.cn-north-1.compute.amazonaws.com.cn:8545","http://94.130.66.112:8545","http://128.199.139.57:8545","http://ec2-13-124-139-36.ap-northeast-2.compute.amazonaws.com:8545","http://101.37.162.87:8545","http://ec2-18-179-189-84.ap-northeast-1.compute.amazonaws.com:8545","http://209.97.177.161:8545","http://47.90.203.226:8545","http://47.254.157.139:8545","http://oki-180-131-208-217.jptransit.net:8545","http://54.169.39.25:8545","http://47.74.247.110:8545","http://47.75.9.16:8545","http://59.110.212.17:8545","http://18.231.185.118:8545","http://116.62.13.186:8545","http://39.105.140.1:8545","http://47.91.252.103:8545","http://ec2-52-15-167-99.us-east-2.compute.amazonaws.com:8545","http://47.93.184.213:8545","http://34.215.210.155:8545","http://ec2-35-169-64-78.compute-1.amazonaws.com:8545","http://136.243.19.218:8545","http://172.105.197.89:8545","http://47.91.230.183:8545","http://18.191.246.98:8545","http://13.210.29.172:8545","http://ec2-13-125-242-67.ap-northeast-2.compute.amazonaws.com:8545","http://ec2-54-210-175-145.compute-1.amazonaws.com:8545","http://122x215x240x181.ap122.ftth.ucom.ne.jp:8545","http://47.96.170.19:8545","http://178.128.174.220:8545","http://45.32.129.224:8545","http://52.224.68.242:8545","http://47.75.70.242:8545","http://39.107.29.152:8545","http://ec2-54-185-154-29.us-west-2.compute.amazonaws.com:8545","http://34.204.36.137:8545","http://185.198.57.83:8545","http://139.59.158.0:8545","http://35.184.22.14:8545","http://45.55.50.112:8545","http://101.37.160.222:8545","http://47.96.86.249:8545","http://199-43-184-102.static-ip.telepacific.net:8545","http://ec2-18-219-79-33.us-east-2.compute.amazonaws.com:8545","http://ec2-34-212-139-136.us-west-2.compute.amazonaws.com:8545","http://119.23.201.147:8545","http://114.116.69.178:8545","http://47.88.236.91:8545","http://35.177.61.58:8545","http://188.138.1.43:8545","http://ec2-18-217-146-84.us-east-2.compute.amazonaws.com:8545","http://47.105.53.182:8545","http://54.172.163.110:8545","http://47.75.150.175:8545","http://ec2-34-221-154-226.us-west-2.compute.amazonaws.com:8545","http://206.189.20.131:8545","http://ec2-34-220-193-214.us-west-2.compute.amazonaws.com:8545","http://cz5014.host-telecom.com:8545","http://101.37.163.77:8545","http://ec2-52-70-187-224.compute-1.amazonaws.com:8545","http://111.231.75.170:8545","http://144.217.5.51:8545","http://47.52.246.172:8545","http://150.109.105.170:8545","http://47.75.175.20:8545","http://ec2-35-162-201-130.us-west-2.compute.amazonaws.com:8545","http://47.75.52.8:8545","http://110.185.107.32:8545","http://18.216.102.20:8545","http://52.44.110.239:8545","http://165.227.159.23:8545","http://ec2-35-173-57-26.compute-1.amazonaws.com:8545","http://39.107.60.254:8545","http://101.37.253.219:8545","http://47.52.97.36:8545","http://47.100.63.22:8545","http://147.135.254.199:8545","http://ec2-35-174-18-207.compute-1.amazonaws.com:8545","http://103.75.1.103:8545","http://ec2-54-169-144-165.ap-southeast-1.compute.amazonaws.com:8545","http://static.31.48.201.138.clients.your-server.de:8545","http://ec2-54-91-105-122.compute-1.amazonaws.com:8545","http://116.62.210.86:8545","http://47.90.205.33:8545","http://116.62.13.150:8545","http://114.116.42.165:8545","http://ec2-18-208-64-51.compute-1.amazonaws.com:8545"]
MAX_BLOCK_BACK = 100
MAX_RTT = 5000
outputdir = '../full_matrix/'
f = open(outputdir+'SuccessRate_'+str(MAX_BLOCK_BACK)+'_'+str(MAX_RTT)+'.csv', 'w')
f1 = open(outputdir+'rightBlock_'+str(MAX_BLOCK_BACK)+'_'+str(MAX_RTT)+'.csv', 'w')
f2 = open(outputdir+'recentHeight_'+str(MAX_BLOCK_BACK)+'_'+str(MAX_RTT)+'.csv', 'w')
f3 = open(outputdir+'roundtripTime_'+str(MAX_BLOCK_BACK)+'_'+str(MAX_RTT)+'.csv', 'w')

BlockNumberHash = pd.read_csv("BlockNumberHash.csv")
BlockNumberHash.set_index(["number"], inplace=True)

def eachFile(srcDataPath):
    pathDir =  os.listdir(srcDataPath)
    pd.DataFrame(pathDir).to_csv(outputdir+"ClientsIP.csv",index=False)
    pd.DataFrame(peers).to_csv(outputdir+"PeersIP.csv",index=False)
    cnt=0
    for ip in pathDir:
        readFile(ip)
        cnt += 1
        print(cnt, ip)

def to10(x):
    if (pd.isnull(x)):
        return x
    else:
        return int(x,16)

def validBlock(thisblock):
    try:
        goodhash = BlockNumberHash['hash'][thisblock['number']]
        if (thisblock['hash'] == goodhash):
            return 1
        else:
            return 0
    except:
        #print(thisblock['number'])
        return 0

def readFile(ip):
    global f,f1,f2,f3
    #to df
    jsons=[]
    filename = srcDataPath+ip+"/output.txt"
    fopen = open(filename, 'r') # r 代表read
    for eachLine in fopen:
        jsonstr = '{'+eachLine[:-2]+'}'
        jsons.append(json.loads(jsonstr))
    fopen.close()
    df = pd.DataFrame(jsons)
    df['batchtime']=df['batchtime'].apply(lambda x:int(x))
    df['number']=df['number'].apply(to10)
    df['rightblock'] = df.apply(validBlock, axis=1)

    #init jifen
    jifen = {}
    for peer in peers:
        jifen[peer] = {
            'total': 0,
            'blockTotal':0,
            'rightBlock': 0,
            'recentHeight': 0,
            'inTime': 0,
            'subHeightSum': 0,
            'roundtripTimeSum': 0,
            'success': 0
        }

    #suan batch
    batchs = df.batchtime.unique()
    last_blocknow = 6109000
    for oneBatch in batchs:
        batchDF = df[df.batchtime==oneBatch]
        #print(batchDF)

        #blocknow
        blocknow=0
        for bi in batchDF.index:
            if (batchDF['rightblock'][bi] and batchDF['number'][bi]>blocknow):
                blocknow = batchDF['number'][bi]

        if (blocknow<6109000 or blocknow>6111000):
            blocknow = last_blocknow
        else :
            last_blocknow = blocknow
        #print(blocknow)

        
        for bi in batchDF.index:
            #check
            # if (batchDF['addr'][bi]=="http://47.88.189.195:8545"):
            #     print(blocknow, batchDF['number'][bi], blocknow-batchDF['number'][bi])
            #total
            jifen[batchDF['addr'][bi]]['total'] += 1

            #right block
            bo1 = (batchDF['rightblock'][bi])
            if (bo1):
                jifen[batchDF['addr'][bi]]['rightBlock'] += 1

            #recent height
            bo2 = (blocknow-batchDF['number'][bi]<=MAX_BLOCK_BACK and blocknow-batchDF['number'][bi]>=0)
            if (bo2):
                jifen[batchDF['addr'][bi]]['recentHeight'] += 1

            #intime
            jifen[batchDF['addr'][bi]]['roundtripTimeSum'] += batchDF['endtime'][bi]-batchDF['starttime'][bi]
            bo3 = (batchDF['endtime'][bi]-batchDF['starttime'][bi]<MAX_RTT)
            if (bo3):
                jifen[batchDF['addr'][bi]]['inTime'] += 1

            #success
            if (bo1 and bo2 and bo3):
                jifen[batchDF['addr'][bi]]['success'] += 1

    for peer in peers:
        f.write(str(jifen[peer]['success']/jifen[peer]['total'])+'\t')
        f1.write(str(jifen[peer]['rightBlock']/jifen[peer]['total'])+'\t')
        f2.write(str(jifen[peer]['recentHeight']/jifen[peer]['total'])+'\t')
        f3.write(str(jifen[peer]['roundtripTimeSum']/jifen[peer]['total'])+'\t')

    f.write('\n')
    f1.write('\n')
    f2.write('\n')
    f3.write('\n')

if __name__ == '__main__':
    srcDataPath = "../data_source/"
    eachFile(srcDataPath)
